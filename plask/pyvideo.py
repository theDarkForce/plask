# pyvideo
# create at 2015/6/12
# autor: qianqians
from tools import argv_instance
from pyelement import pyelement

class pyvideo(pyelement):
	def __init__(self, src, cname, layout, praframe):
		self.src = src

		self.type = "video"

		super(pyvideo, self).__init__(cname, layout, praframe)
		
	def flush(self):
		# if img is not none, use img for link, 
		# if img is none, use text for link,
		# this control jump to other page
		# codegen css in page
		shtml = ""
		if self.html is not None:
			shtml = self.html
		else:
			shtml = "<div id=\"" + self.id + "_1\"><video id=\"" + self.id + "\" controls=\"controls\""
		
			for event, onevent in self.uievent:
				shtml += event + "=" + self.id + event + "(this)"

			shtml += "><source src=\"" + self.src + "\" />"
			shtml += "Your browser does not support HTML5 video.</video></div>"

		js = ""
		if self.js is not None:
			js = self.js 
		else:
			for event, onevent in self.uievent.iteritems():
				js += "function " + self.id + event + "(id){"
				for f in onevent:
					js += f
				js += "}\n"
			
		return shtml, js

	def client_set_video(self, src):
		return "id.src = " + src + ";"

	def server_set_video(self, src):
		return "document.getElementById(\"" + self.id + "\").src = " + src + ";"

	def set_default_src(self, src):
		self.src = src 