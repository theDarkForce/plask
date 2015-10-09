# pyfile
# create at 2015/7/2
# autor: qianqians
from pyelement import pyelement

class pyfile(object):
	def __init__(self, file_data, file_name, page):
		self.file_name = file_name
		
		if page is not None:
			page.reslist.append(self)
		self.page = page

		import os
		import sys
		sys.path.append(os.getcwd() + '\plask')
		from appglobal import res_data
		res_data[self.file_name] = file_data

	def flaskflush(self):
		mime = self.file_name[self.file_name.find('.') + 1:]

		sflask = "@app.route('/" + self.file_name + "')\ndef file_" + self.file_name[0:self.file_name.find('.')] + "():\n"
		sflask += "\tfrom io import BytesIO\n\tfrom appglobal import res_data\n\timport traceback\n"
		sflask += "\ttry:\n"
		sflask += "\t\treturn Response(BytesIO(res_data['" + self.file_name + "']), mimetype='" + mime + "')\n"
		sflask += "\texcept:\n"
		sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n"

		return sflask

	def url(self):
		return self.page.url + self.file_name