# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class conciliadoModel(models.Model):
    _name = 'conciliados.view'
    _description = 'conciliados'
    _auto = False
    _rec_name = 'concept'

    bank_id = fields.Many2one('res.bank', string='Banco')
    country_id = fields.Many2one('res.country', string='País')
    date = fields.Date(string='Fecha', default=fields.Datetime.now)
    tax_information = fields.Char(string='RFC')
    account = fields.Char(string='Cuenta')
    amount = fields.Monetary(string='Monto', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Journal Currency')
    type = fields.Char(string='Tipo')
    concept = fields.Selection(string='Concepto', selection=[('Pago de Prestamo', 'Pago de Prestamo'),
                                                             ('Operación 4567', 'Operación 4567'),
                                                             ('OP1234', 'OP1234'),
                                                             ('Pago', 'Pago'),
                                                             ('Pago 2', 'Pago 2'),
                                                             ('Intereses', 'Intereses'),
                                                             ('Operación 4532', 'Operación 4532'),
                                                             ('Pago Financiamiento', 'Pago Financiamiento')])

    #Campos que dependen de la consulta SQL
    _depends = {
        'master_x': [
            'date', 'tax_information', 'amount', 'bank_id', 'country_id',
        ],
        'complemento': [
            'date', 'tax_information', 'account', 'type', 'concept',
        ],
    }

    @property
    def _table_query(self):
        #Consluta sql para union de tablas master_x y complemento
        query = """
            SELECT 
                ma.id,
                ma.amount as amount,
                ma.bank_id as bank_id,
                ma.country_id as country_id,
                ma.tax_information as tax_information,
                co.concept as concept,
                co.type as type,
                co.account as account,
                co.date as date
	            FROM master_x ma 
	            INNER JOIN complemento co ON ma.tax_information = co.tax_information AND
                ma.date = co.date
            """
        return query
