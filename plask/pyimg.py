# pyimg
# create at 2015/5/28
# autor: qianqians
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pyimg(pyelement):
	onclick = 0

	def __init__(self, img, cname, layout, praframe):
		# when normal
		self.normalimg = img
		self.type = "img"
		super(pyimg, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"img\");\n"
		js += " table_" + self.id + ".src=\"" + self.normalimg + "\";\n"

		js += super(pyimg, self).sub()

		if id:
			js += " " + id + ".appendChild(table_" + self.id + ");\n"
		else:
			js += " table_pop.appendChild(table_" + self.id + ");\n"

		return js

	def flush(self):
		# if img is not none, use img for img, 
		# if img is none, use text for img,
		# handle onclick in js and send a requst to service
		# codegen css in page
		shtml = ""
		if self.html is not None:
			shtml = self.html
		else:
			shtml = "<div id=\"" + self.id + "_1\"><img " + "id=\"" + self.id + "\""
			if self.width > 0:
				shtml += " width=" + str(self.width)
			if self.height > 0:
				shtml += " height=" + str(self.height)
			if self.margin == pyhtmlstyle.margin_left:
				shtml += " align=left"
			elif self.margin == pyhtmlstyle.margin_right:
				shtml += " align=right"
			for event, onevent in self.uievent:
				shtml += event + "=" + self.id + event + "(this)"
			shtml += " src=\"" + self.normalimg + "\"/></div>"
		
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

	def client_set_img(self, img):
		return "id.src = " + img + ";"

	def server_set_img(self, img):
		return "document.getElementById(\"" + self.id + "\").src = " + img + ";"

	def set_img(self, img):
		self.img = img
