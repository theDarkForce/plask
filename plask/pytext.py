# pytext
# create at 2015/5/28
# autor: qianqians
from pyhtmlstyle import pyhtmlstyle
from pyelement import pyelement

class pytext(pyelement):
	def __init__(self, text, cname, layout, praframe):
		# when normal
		self.normal_text = text
		self.type = "div"
		
		super(pytext, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"" + self.type + "\");\n"
		js += " var texttable_" + self.id + " = document.createTextNode(\"" + self.normal_text + "\");\n"
		js += " table_" + self.id + ".appendChild(texttable_" + self.id + ");\n"

		js += super(pytext, self).sub()

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
			shtml = "<div id=\"" + self.id + "_1\" "

			for event, onevent in self.uievent.iteritems():
				shtml += event + "=\"" + self.id + event + "(this)\" "

			shtml += ">" + self.normal_text + "</div>"
		
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

	def client_set_text(self, text):
		return "id.innerHTML = " + text + ";"

	def server_set_text(self, text):
		return "document.getElementById(\"" + self.id + "_1\").innerHTML = " + text + ";"

	def client_set_background_color(self, color):
		js = "id.style.backgroundColor=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def server_set_background_color(self, color):
		js = "document.getElementById(\"" + self.id + "_1\").style.backgroundColor=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def set_text_decoration(self, decoration):
		self.normal_decoration = decoration

	def pop_set_text_decoration(self, decoration):
		js = "table_" + self.id + ".style.textDecoration=\"" + decoration + "\";"
		return js

	def client_set_text_decoration(self, decoration):
		js = "id.style.textDecoration=\"" + decoration + "\";"
		return js

	def server_set_text_decoration(self, decoration):
		js = "document.getElementById(\"" + self.id + "_1\").style.textDecoration=\""  + decoration + "\";"
		return js

	def pop_set_text(self, key):
		return "table_" + self.id + ".innerHTML = value[\"" + key  + "\"];"

class pydynamictext(pytext):
	def __init__(self, key, cname, layout, praframe):
		# when normal
		self.key = key
		self.type = "div"

		super(pytext, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"" + self.type + "\");\n"
		js += " var texttable_" + self.id + " = document.createTextNode(value[\"" + self.key + "\"]);\n"
		js += " table_" + self.id + ".appendChild(texttable_" + self.id + ");\n"

		js += super(pytext, self).sub()

		if id:
			js += " " + id + ".appendChild(table_" + self.id + ");\n"
		else:
			js += " table_pop.appendChild(table_" + self.id + ");\n"

		return js