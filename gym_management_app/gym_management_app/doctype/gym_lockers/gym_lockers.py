# Copyright (c) 2023, Watson Kodua Acheampong and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymLockers(Document):
	
	# Limit the number of lockers to 5
	def before_naming(self):
		lockers = frappe.db.get_all('Gym Lockers', fields=['availability'])
		available_lockers = 0

		for locker in lockers:
			if locker.availability == 'Available':
				available_lockers += 1
		
		if int(self.locker_id) > 5:
			frappe.throw(f"Only 5 lockers can be assinged, { available_lockers } currently available")
