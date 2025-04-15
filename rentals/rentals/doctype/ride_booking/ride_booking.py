# Copyright (c) 2025, BWM and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def validate(self):
		if not self.items:
			frappe.throw("Please add at least one item to the ride booking.")
		if not self.rate:
			frappe.throw("Please set the rate for the ride booking.")
		total_distance = 0
		for item in self.items:
			total_distance += item.distance
		self.total_amount = total_distance * self.rate


