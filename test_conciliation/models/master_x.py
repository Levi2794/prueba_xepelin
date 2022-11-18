# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class masterModel(models.Model):
    _name = 'master_x'
    _description = 'master'

    name = fields.Char()
    date = fields.Date(string='Fecha', default=fields.Datetime.now)
    tax_information = fields.Char(string='RFC')
    amount = fields.Monetary(string='Monto', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Journal Currency')
    bank_id = fields.Many2one('res.bank', string='Banco')
    country_id = fields.Many2one('res.country', string='País')
