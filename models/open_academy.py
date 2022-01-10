from odoo import models, fields, api


class OpenAcademy(models.Model):
    _name = 'open.academy'
    _description = 'open_academy.open_academy'
    name = fields.Char(string='Name')

    # Busca todos los datos que tengo en la tabla res_partner = contactos
    # Solo tenemos un profesor
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', help='Este es un profesor')

    # Creamos los estudiantes
    # Un estudiante puede tener un solo curso
    partner_ids = fields.One2many(comodel_name='res.partner', inverse_name='academy_id', string='Partners', help="Este es un estudiante")

    # Relacion MANY2MANY Un estudiante puede tener muchos cursos (Puedo añadir muchos estudiantes a muchos cursos
    # Se crea una tabla el cual tendra 2 columnas)
    partners_ids = fields.Many2many(comodel_name='res.partner', string='Many Partners',
                                    relation='academy_partner_rel',
                                    column1='academy_id',
                                    column2='partner_id')

    # Un curso puede tener un  profesor, y en un curso puede tener muchos estudiantes