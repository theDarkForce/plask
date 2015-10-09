# pybutton
# create at 2015/5/28
# autor: qianqians
from tools import argv_instance, tuple_rbg
from pyelement import pyelement

class pybutton(pyelement):
	def __init__(self, text, cname, layout, praframe):
		# when normal
		self.normaltext = text

		self.type = "button"

		super(pybutton, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"input\");\n"
		js += " table_" + self.id + ".type = \"button\";\n"
		js += " table_" + self.id + ".value=\"" + self.normaltext + "\";\n"

		js += super(pybutton, self).sub()

		if id:
			js += " " + id + ".appendChild(table_" + self.id + ");\n"
		else:
			js += " table_pop.appendChild(table_" + self.id + ");\n"

		return js

	def flush(self):
		# if img is not none, use img for button, 
		# if img is none, use text for button,
		# handle onclick in js and send a requst to service
		# codegen css in page
		shtml = ""

		if self.html is not None:
			shtml = self.html
		else:
			shtml += "<div id=\"" + self.id + "_1\"><button " + "id=\"" + self.id + "\"" + " type=\"button\" "
				
			for event, onevent in self.uievent.iteritems():
				shtml += event + "=\"" + self.id + event + "(this)\" "

			shtml += ">" + self.normaltext + "</button></div>"

		js = ""
		if self.js is not None:
			js = self.js
		else:
			for event, onevent in self.uievent.iteritems():
				js += "function " + self.id + event + "(id){"
				js += onevent
				js += "}\n"
		return shtml, js

	def client_set(self, text, textcolor, backcolor):
		js = "id.value=\"" + text + "\";"
		js += "id.style.color=" + tuple_rbg(textcolor) + ";"
		js += "id.style.backgroundColor=" + tuple_rbg(backcolor) + ";"
		return js

	def server_set(self, text, textcolor, backcolor):
		js = "document.getElementById(\"" + self.id + "\").value=\"" + text + "\";\n"
		js += "document.getElementById(\"" + self.id + "\").style.color=" + tuple_rbg(textcolor) + ";\n"
		js += "document.getElementById(\"" + self.id + "\").style.backgroundColor=" + tuple_rbg(backcolor) + ";\n"
		return js
