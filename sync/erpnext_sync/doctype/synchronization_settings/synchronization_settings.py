# -*- coding: utf-8 -*-
# Copyright (c) 2015, Bai Web and Mobile Lab and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from sync.frappeclient import FrappeClient
from sync.utils import sync_doctype


class SynchronizationSettings(Document):

    def validate(self):
        if self.sync_mode == 'Slave':
            if not self.master_url or not self.username or not self.password:
                frappe.throw('URL, username and password should have a value')
            try:
                FrappeClient(self.master_url, self.username, self.password)
            except:
                frappe.throw('Error connecting server')

            sync_doctype('Synchronization DocType', '1976-01-01', 1)








