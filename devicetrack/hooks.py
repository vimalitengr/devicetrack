# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "devicetrack"
app_title = "Device Tracking"
app_publisher = "August Infotech"
app_description = "Device Tracking"
app_icon = "octicon octicon-circuit-board"
app_color = "#D10056"
app_email = "info@augustinfotech.com"
app_license = "GNU General Public Licence"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/devicetrack/css/devicetrack.css"
# app_include_js = "/assets/devicetrack/js/devicetrack.js"

# include js, css files in header of web template
# web_include_css = "/assets/devicetrack/css/devicetrack.css"
# web_include_js = "/assets/devicetrack/js/devicetrack.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "devicetrack.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "devicetrack.install.before_install"
# after_install = "devicetrack.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "devicetrack.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"cron": {
		"*/3 * * * *": [
			"devicetrack.device_tracking.doctype.api_test_environment.api_test_environment.entry_using_api_call"
		]
	}

# 	"all": [
# 		"devicetrack.tasks.all"
# 	],
# 	"daily": [
# 		"devicetrack.tasks.daily"
# 	],
# 	"hourly": [
# 		"devicetrack.tasks.hourly"
# 	],
# 	"weekly": [
# 		"devicetrack.tasks.weekly"
# 	]
# 	"monthly": [
# 		"devicetrack.tasks.monthly"
# 	]
}




# scheduler_events = {
# 	"all": [
# 		"devicetrack.tasks.all"
# 	],
# 	"daily": [
# 		"devicetrack.tasks.daily"
# 	],
# 	"hourly": [
# 		"devicetrack.tasks.hourly"
# 	],
# 	"weekly": [
# 		"devicetrack.tasks.weekly"
# 	]
# 	"monthly": [
# 		"devicetrack.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "devicetrack.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "devicetrack.event.get_events"
# }

