#gen by plask
#a new html framework
#web service code
from flask import *
from serviceapp import app

@app.route('/edittest')
@app.route('/')
def edittestindex():
	import os
	file = open("./html/edittest.html")
	return file.read()

@app.route('/button/submit',methods=['POST'])
def buttonsubmit():
	import traceback
	from appglobal import cb_mothed
	from io import BytesIO
	import json
	r = {}
	try:
		for cb in cb_mothed["button"]["submit"]:
			r.update(cb(request.get_json()))
		return Response(BytesIO(json.dumps(r)), mimetype='text/json')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSON.js')
def file_JSON():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSON.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONError.js')
def file_JSONError():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONError.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONRequest.js')
def file_JSONRequest():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONRequest.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

@app.route('/JSONRequestError.js')
def file_JSONRequestError():
	from io import BytesIO
	from appglobal import res_data
	import traceback
	try:
		return Response(BytesIO(res_data['JSONRequestError.js']), mimetype='js')
	except:
		from log import log
		log(traceback.format_exc())

