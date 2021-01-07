from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class VmLibraryCardType(models.Model):
    _name = "vm.library.card.type"
    _description = "Library Card Type"

    name = fields.Char('Name' ,size=256, required=True)
    allow_media=fields.Integer('No of medias Allowed', size=10, required=True)
    duration=fields.Integer('Duration',help='Durationin terms of Number of Lead Days',required=True)
    penalty_amt_per_day=fields.Float('Penalty Amount per Day', required=True)

    @api.constrains('allow_media', 'duration', 'penalty_amt_per_day')
    def check_details(self):
        if self.allow_media < 0 or self.duration < 0.0 or \
                self.penalty_amt_per_day < 0.0:
            raise ValidationError(_('Enter proper value'))


class VmLibraryCard(models.Model):
    _name= "vm.library.card"
    _rec_name="number"
    _description="Library Card"

    # partner_id = fields.Many2one('res.partner', 'Student/Faculty', required=True)
    number = fields.Char('Number', size=256, readonly=True)
    # library_card_type_id = fields.Many2one('vm.library.card.type','Card Type',required=True)
    # issue_date =fields.Date('Issue Date', required=True,default=fields.Date.today())
    type = fields.Selection(
        [('student', 'Student'),('faculty','Faculty')],
        'Type', default='student',required=True)

    # student_id = fields.Many2one('op.student', 'Student',domain = [('library_card_id', '=', False)])
    # faculty_id = fields.Many2one('op.faculty', 'Faculty',domain = [('library_card_id', '=', False)])
    active = fields.Boolean(default=True)
