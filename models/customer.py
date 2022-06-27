#Pridanie jedného nového fieldu(dropdownu) na databázu res.partner

from odoo import models , fields

class Customer(models.Model):
    _inherit = 'res.partner'
    vyber = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('r', 'R')] , required=True , default = "a")

