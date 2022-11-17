# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class complementoModel(models.Model):
    _name = 'complemento'
    _description = 'complemento'
    _rec_name = 'concept'

    name = fields.Char()
    date = fields.Date(string='Fecha', default=fields.Datetime.now)
    tax_information = fields.Char(string='RFC')
    account = fields.Char(string='Cuenta')
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