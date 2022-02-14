from odoo import models , fields

class LogHistory(models.Model):
    _name = 'log.history'
    _rec_name = 'created_by'

    created_by = fields.Char()
    date = fields.Date()
    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')