# pycontainer
# create at 2015/5/28
# autor: qianqians
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pycontainer(pyelement):
	def __init__(self, cname, layout, praframe):
		self.backcolor = 0
		self.divlist = []

		self.width = 0
		self.height = 0

		super(pycontainer, self).__init__(cname, layout, praframe)

	def sub(self, id = None):
		js = " var table_" + self.id + " = document.createElement(\"div\");\n" + super(pycontainer, self).sub()
		for div in self.divlist:
			js += div.sub("table_" + self.id)

		if id:
			js += " " + id + ".appendChild(table_" + self.id + ");\n"
		else:
			js += " table_pop.appendChild(table_" + self.id + ");\n"

		return js

	def set_backcolor(self, color):
		self.backcolor = color

	def set_size(self, width, height):
		self.width = width
		self.height = height
		
	def register_event(self, event, onevent):
		raise "container can post any event"
	
	def flaskflush(self):
		flask = ""
		for div in self.divlist:
			flask += div.flaskflush() 
		return flask

	def client_set_visible(self, isvisible):
		if isvisible:
			code = "id.style.visibility=\"visible\";\n"
			code += "for(var i=0;i<id.childNodes.length;i++){"
			code += "   id.childNodes[i].style.visibility=\"visible\";\n}"
			return code
		else:
			code = "id.style.visibility=\"hidden\";\n"
			code += "for(var i=0;i<id.childNodes.length;i++){"
			code += "   id.childNodes[i].style.visibility=\"hidden\";\n}"
			return code

	def server_set_visible(self, isvisible):
		if isvisible:
			code = "document.getElementById(\"" + self.id + "_1\").style.visibility=\"visible\";\n"
			code += "for(var i=0;i<document.getElementById(\"" + self.id + "_1\").childNodes.length;i++){"
			code += "   document.getElementById(\"" + self.id + "_1\").childNodes[i].style.visibility=\"visible\";\n}"
			return code
		else:
			code = "document.getElementById(\"" + self.id + "_1\").style.visibility=\"hidden\";\n"
			code += "for(var i=0;i<document.getElementById(\"" + self.id + "_1\").childNodes.length;i++){"
			code += "   document.getElementById(\"" + self.id + "_1\").childNodes[i].style.visibility=\"hidden\";\n}"
			return code

	def gencss(self):
		scss =  self.cssstyle() + self.csslayout()
		if self.clear:
			scss += " clear:both;}"
		else:
			scss += " }"
		count = 0
		margin = None

		width = 0

		for div in self.divlist:
			if isinstance(div, pycontainer):
				scss += div.gencss()
			else:
				if margin != div.margin:
					margin = div.margin
					if count != 0:
						count = 0

				if div.margin == pyhtmlstyle.float_left:
					if count != 0 and div.border_style is not None:
						scss += div.cssstyle() + div.csslayout() + " border-left-style: none;}"
					else:
						scss += div.cssstyle() + div.csslayout() + " }"
					count += 1

					if self.width > 0:
						width += div.width
						if width >= self.width:
							width = 0
							count = 0
				elif div.margin == pyhtmlstyle.float_right:
					if count != 0 and div.border_style is not None:
						scss += div.cssstyle() + div.csslayout() + " border-right-style: none;}"
					else:
						scss += div.cssstyle() + div.csslayout() + " }"
					count += 1

					if self.width > 0:
						width += div.width
						if width >= self.width:
							width = 0
							count = 0
				else:
					scss += div.cssstyle() + div.csslayout() + "}"

		return scss	
		
	def flush(self):
		# if img is not none, use img for container, 
		# if img is none, use text for container,
		# codegen css in page
		html = "<div id=\"" + self.id + "_1\">"
		script = ""
		for div in self.divlist:
			sshtml,sjs = div.flush()
			html += sshtml
			script += sjs
		html += "</div>"
			
		return html,script