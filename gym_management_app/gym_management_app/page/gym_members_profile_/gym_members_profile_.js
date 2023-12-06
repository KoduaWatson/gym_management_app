frappe.pages['gym_members_profile_'].on_page_load = function(wrapper) {
	new MyPage(wrapper); 





// my_custom_app/my_module/page/my_custom_page/my_custom_page.js

// frappe.pages['my-custom-page'].on_page_load = function(wrapper) {
//     // Your JavaScript logic here

    
// };

//PAGE CONTENT

MyPage = Class.extend({
	init: function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper, 
			title: 'Gym Members Profile Page',
			single_column: true
		});
		//make page
		this.make();
	},
	//make page
	make: function(){
		//grab the class
		let me = $(this);

		//body content
		let body = `<h1>create</h1> `;

		//get membership details
		let membership_details = function() {
			frappe.call({
				method:"gym_management_app.gym_management_app.page.\
					gym_members_profile_.gym_members_profile_.get_membership_data",
				callback: function(r) {
					console.log(r)
				}
			})
		}

		frappe.call({
			method: "gym_management_app.gym_management_app.page.\
			gym_members_profile_.gym_members_profile_.get_membership_data",
			callback: function(response) {
				// Handle the response from the server
				if (response.message) {
					console.log(response)
					// Render the data using frappe.render_template
					//const rendered_html = frappe.render_template('my_custom_page_result', { message: response.message });
					
					// Append the rendered HTML to the container
					//$(wrapper).find('#custom-data-container').html(rendered_html);
				}
			}
		});
				

		// let params = {
		// 	pagename: "gym_management_app/gym_management_app/page/gym_members_profile_.html"
		// }

		// let html_content = function(){
		// 	frappe.call({
		// 		method:("gym_management_app.gym_management_app.page.\
		// 		gym_members_profile_.gym_members_profile_.get_html_content",params), 
		// 		callback:function(data) {
		// 			console.log(`Message is : ${data.message}`)
		// 		}
		// 		//.then((data) => {
		// 			//$("#gym_members_profile_").html(data.message);
		// 		});
		// 	}

		//push dom element to page
		//$(frappe.render_template("gym_members_profile_", this)).appendTo(this.page.main)


			//html_content();
		membership_details();
	}

		

	//end of class
})
}

//HTML CONTENT
//frappe.gym_management_app = {}
// frappe.gym_management_app = {
// 		body: body
// };