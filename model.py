from odoo import models, fields

class DurableRecord(models.Model):
    _name = "durable.durable"
    id = fields.Integer(string='ID')
    name = fields.Char(string='Name', required=True)
    model = fields.Char(string='Model Name', required=True)
    photo = fields.Binary(string='Photo')
    qr_code = fields.Binary(string='Qr code')
    receive_date = fields.Date(string="Receive_date")
    type = fields.Selection([('Eq', 'Equipment/measure'), ('F', 'Furniture'),('Infor', 'Information equipment')], ('O', 'Other'), string='type')
    room_type = fields.Selection([('M', 'Meeting room'), ('C', 'Classroom'), ('L', 'Laboratory'), ('T', 'Teacher room')], string='room_type')
    room = fields.Selection([('R1', 'Room1'), ('R2', 'Room2'), ('L1', 'Lab1'), ('L2', 'Lab2')], string='room')
    status = fields.Selection([('A', 'Available'), ('P', 'Prepare to sell'), ('S', 'Sold'), ('D', 'Damaged')], string='status')


