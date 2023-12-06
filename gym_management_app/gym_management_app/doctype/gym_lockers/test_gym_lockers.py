# Copyright (c) 2023, Watson Kodua Acheampong and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymLockers(FrappeTestCase):

	
	def create_locker_id_6(self):

		#Try creating locker with id 6
		self.assertEqual(frappe.get_doc(doctype='Gym Lockers', locker_id = '6'))

		#Now try creating locker with id 5
		self.assertEqual(frappe.get_doc(doctype='Gym Lockers', locker_id = '5'))

		
