from odoo import models,fields,api
from odoo.exceptions import UserError

class Customer(models.Model):
    _inherit = 'res.partner'

    related_patient_id=fields.Many2one('hms.patient')

    @api.constrains('related_patient_id')
    def customer_email_check(self):
        if self.email == self.related_patient_id.email:
            raise UserError("email already exist")

    def unlink(self):
        if self.related_patient_id:
            raise UserError("You can't delete linked patient")
        super().unlink()



