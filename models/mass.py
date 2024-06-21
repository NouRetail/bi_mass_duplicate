# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api

class MassSale(models.Model):
	_name = 'mass.duplicate'

	def mass_copy(self,vals):
		order_ids=[]
		model = None
		for i in vals:
			order_ids.append(i['data']['id'])
			model = i['model']
		order = self.env[model].browse(order_ids)
		for odr in order:
			odr.copy()
		return