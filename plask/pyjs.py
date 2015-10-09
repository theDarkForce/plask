# pyfile
# create at 2015/7/2
# autor: qianqians
from pyelement import pyelement
from pyfile import pyfile

class pyjs(object):
	def __init__(self, url):
		import os
		filejson = open(os.path.split(os.path.realpath(__file__))[0] + '/jsonrequest/JSON.javascript', 'rb')
		json = filejson.read()
		filejson.close()

		fileJSONError = open(os.path.split(os.path.realpath(__file__))[0] + '/jsonrequest/JSONError.javascript', 'rb')
		JSONError = fileJSONError.read()
		fileJSONError.close()

		fileJSONRequest = open(os.path.split(os.path.realpath(__file__))[0] + '/jsonrequest/JSONRequest.javascript', 'rb')
		JSONRequest = fileJSONRequest.read()
		fileJSONRequest.close()

		fileJSONRequestError = open(os.path.split(os.path.realpath(__file__))[0] + '/jsonrequest/JSONRequestError.javascript', 'rb')
		JSONRequestError = fileJSONRequestError.read()
		fileJSONRequestError.close()

		import sys
		sys.path.append(os.getcwd() + '\plask')
		from appglobal import res_data
		res_data['JSON.js'] = json
		res_data['JSONError.js'] = JSONError
		res_data['JSONRequest.js'] = JSONRequest
		res_data['JSONRequestError.js'] = JSONRequestError

		self.url = url

	def flaskflush(self):
		mime = "js"

		sflask = "@app.route('/" + 'JSON.js' + "')\ndef file_" + 'JSON' + "():\n"
		sflask += "\tfrom io import BytesIO\n\tfrom appglobal import res_data\n\timport traceback\n"
		sflask += "\ttry:\n"
		sflask += "\t\treturn Response(BytesIO(res_data['JSON.js']), mimetype='" + mime + "')\n"
		sflask += "\texcept:\n"
		sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n\n"	

		sflask += "@app.route('/" + 'JSONError.js' + "')\ndef file_" + 'JSONError' + "():\n"
		sflask += "\tfrom io import BytesIO\n\tfrom appglobal import res_data\n\timport traceback\n"
		sflask += "\ttry:\n"
		sflask += "\t\treturn Response(BytesIO(res_data['JSONError.js']), mimetype='" + mime + "')\n"
		sflask += "\texcept:\n"
		sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n\n"	

		sflask += "@app.route('/" + 'JSONRequest.js' + "')\ndef file_" + 'JSONRequest' + "():\n"
		sflask += "\tfrom io import BytesIO\n\tfrom appglobal import res_data\n\timport traceback\n"
		sflask += "\ttry:\n"
		sflask += "\t\treturn Response(BytesIO(res_data['JSONRequest.js']), mimetype='" + mime + "')\n"
		sflask += "\texcept:\n"
		sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n\n"	

		sflask += "@app.route('/" + 'JSONRequestError.js' + "')\ndef file_" + 'JSONRequestError' + "():\n"
		sflask += "\tfrom io import BytesIO\n\tfrom appglobal import res_data\n\timport traceback\n"
		sflask += "\ttry:\n"
		sflask += "\t\treturn Response(BytesIO(res_data['JSONRequestError.js']), mimetype='" + mime + "')\n"
		sflask += "\texcept:\n"
		sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n\n"	

		return sflask

	def JSON_url(self):
		return self.url + 'JSON.js'

	def JSONError_url(self):
		return self.url + 'JSONError.js'

	def JSONRequest(self):
		return self.url + 'JSONRequest.js'

	def JSONRequestError_url(self):
		return self.url + 'JSONRequestError.js'