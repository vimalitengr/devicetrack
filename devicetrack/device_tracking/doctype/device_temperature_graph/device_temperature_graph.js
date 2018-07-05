// Copyright (c) 2018, August Infotech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Device Temperature Graph', {
	refresh: function(frm) {	
		frm.disable_save();	
		// cur_frm.set_value("from_date",frappe.datetime.add_months(frappe.datetime.get_today(), -1),)
	},
	generate: function(frm) {
		if(!frm.doc.from_date || !frm.doc.to_date){
			frappe.throw("Please Select Dates to get Chart")
		}else{
			var data_values = []
				frappe.call({
					doc: frm.doc,
					"method": "get_chart_data",
					callback: function(r) {
						if(r.message){
							data_values = r.message
							// console.log(data_values)
						
				
							$.getScript("https://www.gstatic.com/charts/loader.js", function(){
							google.charts.load('current', {'packages':['bar']});
							google.charts.setOnLoadCallback(drawChart);
							function drawChart() {
							    var data = new google.visualization.arrayToDataTable(data_values);
							    // data.addColumn('date', 'Day');
      					// 		data.addColumn('number', 'Temperatue');
      							// data.addRows(data_values);
      							
						        var options = {						       
         						 height: 3000,
								 // width: 900,
								bars:'horizontal',
								theme: 'material',	
						          chart: {
						            title: 'Date-Time wise Temperature',			         			  
						          },						        
						        };

								   var chart = new google.charts.Bar($('[title=chart]')[0]);
								    chart.draw(data, options);

								  }
							});							
						}

						   	var my_div = document.getElementById('chart');
						    var my_chart = new google.visualization.ChartType(chart);

						    google.visualization.events.addListener(my_chart, 'ready', function () {
						      my_div.innerHTML = '<img src="' + my_chart.getImageURI() + '">';
						    });

						    my_chart.draw(data);
					}
				})
			}
		}
	});
