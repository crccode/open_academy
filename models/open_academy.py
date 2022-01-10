from odoo import models, fields, api


class OpenAcademy(models.Model):
    _name = 'open.academy'
    _description = 'open_academy.open_academy'
    name = fields.Char(string='Name')