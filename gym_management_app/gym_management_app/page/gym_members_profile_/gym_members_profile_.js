frappe.pages['gym-members-profile-'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Members with Active Membership',
		single_column: true
	});


	
	page.set_primary_action("Save", () => {
		console.log("Save button clicked")
	})


	let field = page.add_field({
		label: 'Document Type',
		fieldtype: 'Link',
		fieldname: 'document_type',
		options: 'Gym Membership'
		,
		change() {
			console.log(field.get_value());
		}
	});
	
}

// frappe.call('gym_management_app.gym_management_app.gym_management_app.page.\
// 			gym_members_profile_.gym_members_profile_.get_membership').then((r) => {
// 				let membership_data = r.message;
// 			})