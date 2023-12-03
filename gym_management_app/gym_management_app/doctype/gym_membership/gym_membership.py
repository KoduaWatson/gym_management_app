# Copyright (c) 2023, Watson Kodua Acheampong and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import add_to_date



class GymMembership(Document):
	def before_save(self):
		
		member_id = self.member_id

		#compute member dob to compute age
		member_dob = frappe.db.get_value('Gym Member', member_id, 'dob')

		today = datetime.now().date()
		self.age = today.year - member_dob.year - ((today.month, today.day) < (member_dob.month, member_dob.day))


		#compute membership end date based on membership type subscribed
		type_of_membership = self.type_of_membership
		
		if type_of_membership == 'Annual':
			self.end_date = add_to_date(datetime.now(), years=1, as_string=True)
		elif type_of_membership == 'Biannual':
			self.end_date = add_to_date(datetime.now(), months=6, as_string=True)
		elif type_of_membership == 'Quarterly':
			self.end_date = add_to_date(datetime.now(), months=3, as_string=True)
		elif type_of_membership == 'Monthly':
			self.end_date = add_to_date(datetime.now(), months=1, as_string=True)
		else:
			self.end_date = add_to_date(datetime.now(), days=1, as_string=True)

