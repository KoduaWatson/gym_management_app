import frappe

all_memberships = frappe.db.get_all('Gym Membership', pluck='name')


