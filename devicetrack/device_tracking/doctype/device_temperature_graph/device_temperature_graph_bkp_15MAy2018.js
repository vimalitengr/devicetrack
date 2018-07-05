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
							
							new_data_values = []
							for (i = 2; i < data_values.length; i++) { 
								new_data_values.push([data_values[i][0].toDate("yyyy-mm-dd hh:ii:ss"), data_values[i][1]])
								// console.log(data_values[i][0].toDate("yyyy-mm-dd hh:ii:ss"))
							}
											


							$.getScript("https://www.gstatic.com/charts/loader.js", function(){
							google.charts.load('current', {'packages':['bar']});
							google.charts.setOnLoadCallback(drawChart);
							function drawChart() {
							    var data = new google.visualization.DataTable();
							    data.addColumn('date', 'Day');
      							data.addColumn('number', 'Temperatue');
      							data.addRows(new_data_values)
						        var options = {						       
         						 height: 300,
								 // width: 900,
								 // bars:'horizontal',
								 theme: 'material',
								  // legend: {'position':'bottom'},
								 hAxis: {
								 	viewWindow: {
							            min: frm.doc.from_date.toDate("yyyy-mm-dd hh:ii:ss"),
							            max: frm.doc.to_date.toDate("yyyy-mm-dd hh:ii:ss")
							          },
							    slantedText: true,  /* Enable slantedText for horizontal axis */
       					        slantedTextAngle: 90, /* Define slant Angle */  
						            format: 'M/d/yy',
						            gridlines: {count: 15}
						          },
						         chart: {
						            title: 'Date-Time wise Temperature',

						          },
								  
						        };

								   var chart = new google.charts.Bar($('[title=chart]')[0]);
								    chart.draw(data, options);

								  }
							});							
						}

						   	// var my_div = document.getElementById('chart');
						    // var my_chart = new google.visualization.ChartType(chart);

						    // google.visualization.events.addListener(my_chart, 'ready', function () {
						    //   my_div.innerHTML = '<img src="' + my_chart.getImageURI() + '">';
						    // });

						    // my_chart.draw(data);
					}
				})
			}
		},


	});
String.prototype.toDate = function(format)
{
  var normalized      = this.replace(/[^a-zA-Z0-9]/g, '-');
  var normalizedFormat= format.toLowerCase().replace(/[^a-zA-Z0-9]/g, '-');
  var formatItems     = normalizedFormat.split('-');
  var dateItems       = normalized.split('-');

  var monthIndex  = formatItems.indexOf("mm");
  var dayIndex    = formatItems.indexOf("dd");
  var yearIndex   = formatItems.indexOf("yyyy");
  var hourIndex     = formatItems.indexOf("hh");
  var minutesIndex  = formatItems.indexOf("ii");
  var secondsIndex  = formatItems.indexOf("ss");

  var today = new Date();

  var year  = yearIndex>-1  ? dateItems[yearIndex]    : today.getFullYear();
  var month = monthIndex>-1 ? dateItems[monthIndex]-1 : today.getMonth()-1;
  var day   = dayIndex>-1   ? dateItems[dayIndex]     : today.getDate();

  var hour    = hourIndex>-1      ? dateItems[hourIndex]    : today.getHours();
  var minute  = minutesIndex>-1   ? dateItems[minutesIndex] : today.getMinutes();
  var second  = secondsIndex>-1   ? dateItems[secondsIndex] : today.getSeconds();

  return new Date(year,month,day,hour,minute,second);
};