import frappe

# for all submitted recs without allocated trainer/trainer contact values, set them to 
# "Patch Trainer" and "pt@gymmail.com"
def execute():
    all_memberships = frappe.db.get_all('Gym Membership', fields=['name', 'allocated_trainer'\
                                    , 'trainer_contact'], filters={'docstatus': 1})
    for membership in all_memberships:
        frappe.db.set_value('Gym Membership', membership.name,{'docstatus': 2,\
                            'allocated_trainer': 'Patch Trainer',\
                            'trainer_contact': 'pt@gymmail.com'})                                 