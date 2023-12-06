import frappe
from frappe.utils import getdate

@frappe.whitelist()
def get_membership_data():
    data = frappe.db.get_all('Gym Membership', fields = \
                             ['member_name', 'member_id', 'start_date', 'end_date', \
                            'allocated_trainer', 'trainer_contact', 'workout_plan'])
    return data


@frappe.whitelist()
def get_todays_date():
    today = getdate()
    return today


@frappe.whitelist()
def get_html_content():
    return frappe.render_template("gym_management_app/gym_management_app/page/gym_members_profile_.html")

