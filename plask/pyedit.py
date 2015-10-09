# pyedit
# create at 2015/6/14
# autor: qianqians
from tools import argv_instance
from pyelement import pyelement

class pyedit(pyelement):
	# edit input type
	text = "text"
	password = "password"
	textarea = "textarea"

	#event
	oninput = "oninput"
	onkeydown = "onkeydown"

	def __init__(self, cname, type, layout, praframe):
		self.type = type
		super(pyedit, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"input\");\n"
		js += " table_" + self.id + ".type = \"" + self.type + "\";\n"

		js += super(pyedit, self).sub()

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
			if self.type == pyedit.textarea:
				shtml += "<div id=\"" + self.id + "_1\"><textarea id=\"" + self.id + "\""
			else:
				shtml += "<div id=\"" + self.id + "_1\"><input id=\"" + self.id + "\" type=\"" + self.type + "\""

			for event, onevent in self.uievent.iteritems():
				shtml += event + "=" + self.id + event + "(this)"
			if self.width > 0 and self.height > 0:
				shtml += " style=\"height:" + str(self.height) + "px;width:" + str(self.width) + "px\""

			if self.type == pyedit.textarea:
				shtml += "></textarea></div>"
			else:
				shtml += "></div>"
		
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

	def client_get_input_text(self):
		return "document.getElementById(\"" + self.id + "\").value"

	def client_set_input_text(self, text):
		return "id.value=\"" + text + "\";\n"

	def server_get_input_text(self, text_key):
		return "document.getElementById(\"" + self.id + "\").value=value[\"" + text_key + "\"];\n"

	def pop_get_input_text(self):
		return " table_" + self.id + ".value\n"