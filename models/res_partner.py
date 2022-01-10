from odoo import models, fields, api

class ResPartner(models.Model):
    # Heredamos del res_partner y creamos la relacion inversa del One2Many
    _inherit = 'res.partner'
    academy_id = fields.Many2one(comodel_name='open.academy', string='Academy')

    # Relacion MANY2MANY inversa
    academies_ids = fields.Many2many(comodel_name='open.academy', string='Academies',
                                    relation='academy_partner_rel',
                                    column1='partner_id',
                                    column2='academy_id')
