# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Provider(models.Model):
    _name = 'provider'
    products = fields.Many2many("product")
    reg_region = fields.Char()
    date_reg = fields.Date()
    email = fields.Char()
    telephone = fields.Char()
    inn = fields.Char()

    circulation = fields.Char()
    product = fields.Char()
    tenders = fields.Selection([("да", "Да"), ("нет", "Нет")])
    contracts_sum = fields.Integer()
    warehouse = fields.Selection([("да", "Да"), ("нет", "Нет")])

    
    contracts_count = fields.Integer()
    contracts_amount = fields.Integer()
    intime_count = fields.Integer()
    intime_amount = fields.Integer()
    cancelled_count = fields.Integer()
    cancelled_amount = fields.Integer()  
    
class Product(models.Model):
    _name = 'product'
    product = fields.Char()
    identify = fields.Integer()
    call = fields.Selection([("да", "Да"), ("нет", "Нет")])
    date = fields.Date()
    status = fields.Selection([("отправлен", "Отправлен"), ("доставлен", "Доставлен")])
    answer = fields.Char()
    price = fields.Char()
    comment = fields.Char() 


    
