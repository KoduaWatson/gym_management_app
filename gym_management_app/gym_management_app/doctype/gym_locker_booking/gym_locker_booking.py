# Copyright (c) 2023, Watson Kodua Acheampong and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today
from frappe.utils import getdate


class GymLockerBooking(Document):
	def before_save(self):

		#set locker availability to Booked after subscription
		frappe.db.set_value('Gym Lockers', self.locker_id, 'availability', 'Booked' )

		#use locker booking end_date to set locker subscription expiry
		booking_expiry = self.expiry
		if getdate(booking_expiry) < getdate(today()):
			frappe.db.set_value('Gym Lockers', self.locker_id, 'availability' 'Available')


