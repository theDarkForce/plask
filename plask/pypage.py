# -*- coding: UTF-8 -*-
#  pypage
# create at 2015/5/28
# autor: qianqians
from pyhtmlstyle import pyhtmlstyle
from pyjs import pyjs
from pysession import *
import pymsgbox

class pypage(pyhtmlstyle):
	def __init__(self, cname, url, layout):
		self.url = url
		self.divlist = []
		self.reslist = []
		self.html = ""
		self.pagename = cname

		self.page_route = []

		self.jsdata = pyjs(self.url)

		self.css = None
		self.html = None
		self.js = None

		super(pypage, self).__init__(cname, layout)

	def init(self):
		import os
		if not os.path.exists('./html'):
			os.makedirs('./html')
		htmlname = "./html/" + self.pagename + ".html"
		fp = open(htmlname, 'w')
		fp.write(self.flush())
		
		if not os.path.exists('./plask'):
			os.makedirs('./plask')
		flaskname = './plask/' + self.pagename + "_1.py"
		fp = open(flaskname, 'w')
		fp.write(self.flaskflush())

		if not os.path.exists('./plask'):
			os.makedirs('./plask')
		servicename = './plask/' + "serviceapp.py"
		fp = open(servicename, 'a')
		fp.write("import " + self.pagename + "_1")

	def add_page_route(self, route):
		self.page_route.append(route)
		
	def flaskflush(self):
		flask = "# -*- coding: UTF-8 -*-\n#gen by plask\n#a new html framework\n#web service code\nfrom flask import *\nfrom serviceapp import app\n"
		import os
		path = os.path.split(os.path.realpath(__file__))[0]
		flask += "import sys\nsys.path.append('" + path + "')\n"
		flask += "import time\nimport pysession\n\n"
		flask += "llid = []\n"
		flask += "llid.append(1)\n"
		flask += "def create_sessionid(ip):\n"
		flask += "\t#获取unix时间戳\n"
		flask += "\tid = str(int(time.time()))\n"
		flask += "\t#用户IP\n"
		flask += "\tid += '-' + ip\n"
		flask += "\t#序列号\n"
		flask += "\tid += '-' + str(llid[0])\n"
		flask += "\tllid[0] += 1\n"
		flask += "\treturn id, llid[0]\n\n"
		flask += "def create_session(ip):\n"
		flask += "\tid,sid = create_sessionid(ip)\n"
		flask += "\tpysession.session[id] = {}\n"
		flask += "\tpysession.session[id][\"ip\"] = ip\n"
		flask += "\tpysession.session[id][\"llid\"] = sid\n"
		flask += "\tpysession.session[id][\"id\"] = id\n"
		flask += "\tprint pysession.session\n"
		flask += "\tjs = \"var sid = \\\"\" + id + \"\\\";\"\n"
		flask += "\treturn js\n\n"
		flask += "@app.route('/" + self.pagename + "')\n"
		for route in self.page_route:
			flask += "@app.route('" + route + "')\n"
		flask += "def " + self.pagename + "index():\n"
		flask += "\tcss = \"\"\"" + self.css + "\"\"\"\n"
		flask += "\thtml = \"\"\"" + self.html + "\"\"\"\n"
		flask += "\tscript = \"\"\"" + self.script + "\"\"\" + create_session(request.remote_addr)" + "\n"
		flask += "\treturn css + html + script + \"</script></html>\"\n\n"
		for div in self.divlist:
			flask += div.flaskflush() 
		for res in self.reslist:
			flask += res.flaskflush()
		flask += self.jsdata.flaskflush()
		return flask
		
	def flush(self):
		scss = "<!DOCTYPE html><html><head><style type=\"text/css\">"
		html = "<body>"
		script = "<script language=\"javascript\" src=\"" + self.jsdata.JSON_url() + "\"></script>"
		script += "<script language=\"javascript\" src=\"" + self.jsdata.JSONError_url() + "\"></script>"
		script += "<script language=\"javascript\" src=\"" + self.jsdata.JSONRequestError_url() + "\"></script>"
		script += "<script language=\"javascript\" src=\"" + self.jsdata.JSONRequest() + "\"></script><script>"
		script += pymsgbox.js_msgbox()

		for div in self.divlist:
			scss += div.gencss()
			
			sshtml,sjs = div.flush()
			html += sshtml
			script += sjs
			
		scss += "</style></head>"
		html += "</body>"

		self.css = scss
		self.html = html
		self.script = script
		
		return scss + html + script + "</script></html>"


