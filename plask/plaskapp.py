# plaskapp
# create at 2015/6/15
# autor: qianqians

class plaskapp(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port 

		import os
		if not os.path.exists('./plask'):
			os.makedirs('./plask')
		servicename = './plask/' + "serviceapp.py"
		fp = open(servicename, 'w')
		fp.write("from flask import *\n\napp = Flask(__name__)\n\n")
		
		resname = './plask/' + "appglobal.py"
		fp = open(resname, 'w')
		fp.write("# res data\nres_data = {}\n\n# callback mothed\ncb_mothed = {}\n")

	def run(self):
		import os
		import sys
		sys.path.append(os.getcwd() + '\plask')
		from serviceapp import app
		
		import traceback
		
		try:
			app.run(self.host, self.port, threaded = True)
		except:
			from log import log
			log(traceback.format_exc())