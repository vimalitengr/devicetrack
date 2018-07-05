// Copyright (c) 2018, August Infotech and contributors
// For license information, please see license.txt

frappe.ui.form.on('API Test Environment', {
	refresh: function(frm) {

	}
});

cur_frm.cscript.click_to_call_api = function(doc,cdt,cdn){
	frappe.call({
		type:"GET",	
		method:"devicetrack.device_tracking.doctype.api_test_environment.api_test_environment.entry_using_api_call",
		args:{
			
		},
		callback:function(r){
			if(r.message){
				
			}
			else
			{
				
			}
		}
	})
}