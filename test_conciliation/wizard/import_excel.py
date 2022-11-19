# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from xlrd import open_workbook
from io import StringIO
from datetime import datetime
from odoo.tools.misc import ustr

import base64
import pandas as pd
import io
import openpyxl
import xlrd


class wizardExcel(models.TransientModel):
    _name = 'wizard.import.excel'
    _description = 'Import Excel'

    date = fields.Date(string='Fecha', default=fields.Datetime.now, readonly=True)
    file = fields.Binary(string='Archivo')
    filename = fields.Char(string='File name')
    user = fields.Many2one('res.users','Usuario', default=lambda self: self.env.user, readonly=True)

    def import_excel(self):
        if not self.file:
            # mensaje de error en caso de no seleccionar ningun archivo
            raise UserError(_('No se seleccionó ningún archivo.'))
        elif self.file:

            # encapsulamos los módelos donde se crearan los registros a partir del archivo xlsx
            master = self.env['master_x']
            complemento = self.env['complemento']

            data = base64.decodestring(self.file)

            #validamos que el archivo sea un .xlsx
            if 'xlsx' not in self.filename:
                raise UserError(_('El archivo solo puede ser un .xlsx'))

            file = pd.read_excel(data)  #Leemos el archivo .xlsx
            campos = file.columns.ravel()   #Extraemos la cabecera del archivo
            datos = file.values     #Extraemos los datos del archivo

            #Validación de existencia de un encabezado
            for c in campos:
                if 'Unnamed' in c:
                    raise UserError(_('El archivo no contiene encabezado'))


            if 'complemento' in self.filename:
                for datos_n in datos:
                    #Validación de campos en balanco
                    for d in datos_n:
                        if 'nan' == str(d):
                            raise UserError(_('El archivo contiene catos en blanco'))

                    #Busqueda para validar registros existentes
                    if complemento.search([('tax_information','=',datos_n[3])]):
                        raise UserError(_('Todos los registros ya se encuentran importados'))

                    #Invocación de metrodo crear del módelo complemento
                    complemento.create({
                        'concept': datos_n[0],
                        'type': datos_n[1],
                        'account': datos_n[2],
                        'tax_information': datos_n[3],
                        'date': datos_n[4]
                    })
            else:
                for datos_n in datos:
                    #Validación de campos en balanco
                    for d in datos_n:
                        if 'nan' == str(d):
                            raise UserError(_('El archivo contiene catos en blanco'))

                    #Busqueda para validar registros existentes
                    if master.search([('tax_information','=',datos_n[1])]):
                        raise UserError(_('Todos los registros ya se encuentran importados'))

                    #Invocación de metrodo crear del módelo master_x
                    master.create({
                        'date': datos_n[0],
                        'tax_information': datos_n[1],
                        'amount': datos_n[2],
                        'bank_id': datos_n[3],
                        'country_id': datos_n[4]
                    })

