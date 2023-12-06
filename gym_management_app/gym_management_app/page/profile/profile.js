// frappe.pages['profile'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Membership Profile Page',
// 		single_column: true
// 	});
// }


frappe.pages['profile'].on_page_load = function(wrapper) {
	new MyPage(wrapper);
}

MyPage = Class.extend({
init: function(wrapper) {
   this.page = frappe.ui.make_app_page({
	   parent: wrapper,
	   title: 'Membership Profile Page',
	   single_column: true
   });
   this.make();
},
make: function() {
   $(frappe.render_template("profile", this)).appendTo(this.page.main);
}
})


//let membership_details = function() {

	// frappe.call({
	// 	method:"gym_management_app.gym_management_app.page.profile.profile.membership_details",
	// 	callback: function(r) {
	// 		//console.log(r)
	// 		let membership_details = r.message
	// 	}
	// 	// membership_details()
	// })
//}

let pagename = "template"

let pagebody = frappe
.call(
  "gym_management_app.gym_management_app.page.template.newprofile.get_profile_html",
  {
	pagename: pagename
  }
)
.then((data) => {
  $("#employee-profile").html(data.message);
});


// membership_details()