frappe.pages['testing-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Display this',
		single_column: true
	});
	
	frappe.call({
		method: "gym_management_app.api.get_data"
	}).then(({message}) => {
		const layout_main = $(wrapper).find(".layout-main");

		html = "<ul>"
		for (let f of message) {
			html += `<li>${f}</li>`
		}
		html += "</ul>"

		layout_main.append(html);
	})

}