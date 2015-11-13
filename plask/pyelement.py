# pyelement
# create at 2015/5/28
# autor: qianqians
from pyhtmlstyle import pyhtmlstyle

class pyelement(pyhtmlstyle):
	# ui event
	onmouseover = "onmouseover"
	onmouseout = "onmouseout"
	onmouseup = "onmouseup"
	onmousedown = "onmousedown"
	onclick = "onclick"

	def __init__(self, cname, layout, praframe):
		if praframe is not None:
			praframe.divlist.append(self)
		self.praframe = praframe

		self.uievent = {}

		super(pyelement, self).__init__(cname, layout)

	def get_obj(self):
		return "document.getElementById(\"" + self.id + "\")"

	def remove(self):
		return self.praframe.get_obj() + ".body.removeChild(msgObj);\n" + self.praframe.get_obj() + ".body.removeChild(table);\n"

	def sub(self):
		js = ""
		isset = False
		left = "auto"
		right = "auto"
		top = "auto"
		bottom = "auto"

		isset = False
		if self.left >= 0:
			isset = True
			left = str(self.left) + "px"
		if self.top >= 0:
			isset = True
			top = str(self.top) + "px"
		if self.right >= 0:
			isset = True
			right = str(self.right) + "px"
		if self.bottom >= 0:
			isset = True
			bottom = str(self.bottom) + "px"

		if isset:
			js += " table_" + self.id + ".style.margin=\"" + top + " " + right + " " + bottom + " " + left + "\";\n"
		if self.margin == pyhtmlstyle.float_left:
			js +=  " table_" + self.id + ".style.float = \"left\";\n"
		if self.margin == self.margin == pyhtmlstyle.float_right:
			js +=  " table_" + self.id + ".style.float = \"right\";\n"
		if self.clear:
			js +=  " table_" + self.id + ".style.clear = \"both\";\n"
		if self.border_size > 0:
			js +=  " table_" + self.id + ".style.borderWidth = \"" + str(self.border_size) + "px\";\n"
		if self.border_style:
			js +=  " table_" + self.id + ".style.borderStyle = \"" + self.border_style + "\";\n"
		if self.border_color:
			js +=  " table_" + self.id + ".style.borderColor = \"rgb(" + str(self.border_color[0]) + "," + str(self.border_color[1]) + "," + str(self.border_color[2]) + ")\";\n"

		if self.border_left_style is not None:
			js +=  " table_" + self.id + ".style.borderLeftStyle = \"" + self.border_left_style + "\";\n"

		if self.border_right_style is not None:
			js +=  " table_" + self.id + ".style.borderRightStyle = \"" + self.border_right_style + "\";\n"

		if self.border_top_style is not None:
			js +=  " table_" + self.id + ".style.borderTopStyle=\"" + self.border_top_style + "\";\n"

		if self.border_bottom_style is not None:
			js +=  " table_" + self.id + ".style.borderBottomStyle=\"" + self.border_bottom_style + "\";\n"

		if self.font_size:
			js += " table_" + self.id + ".style.fontSize=\"" + str(self.font_size) + "%\";\n"

		if self.font_color:
			js += " table_" + self.id + ".style.color=\"rgb(" + str(self.font_color[0]) + "," + str(self.font_color[1]) + "," + str(self.font_color[2]) + ")\";\n"

		if self.normal_decoration:
			js += " table_" + self.id + ".style.textDecoration=\"" + self.normal_decoration + "\";\n"


		for event, onevent in self.uievent.iteritems():
			js += "table_" + self.id + "." + event + "=function() {\n"
			js += onevent
			js += "}\n"

		return js

	def _register_uievent(self, event, onevent):
		self.uievent[event] = onevent
		
	def _register_serverevent(self, sevent, onsevent):
		import os
		import sys
		sys.path.append(os.getcwd() + '\plask')
		from appglobal import cb_mothed
		if not cb_mothed.has_key(self.id):
			cb_mothed[self.id] = {}
		cb_mothed[self.id][sevent] = onsevent
		
	def register_uievent(self, uiev):
		from tools import uievent
		self._register_uievent(uiev.uievent, uiev.get_onevent())
		if len(uiev.server_events) is not 0:
			for s in uiev.server_events:
				self._register_serverevent(s.event, s.cb)

	def client_set_visible(self, isvisible):
		if isvisible:
			return "id.style.visibility=\"visible\";\n"
		else:
			return "id.style.visibility=\"hidden\";\n"

	def server_set_visible(self, isvisible):
		if isvisible:
			return "document.getElementById(\"" + self.id + "\").style.visibility=\"visible\";\n"
		else:
			return "document.getElementById(\"" + self.id + "\").style.visibility=\"hidden\";\n"

	def set_font_color(self, color):
		self.font_color = color

	def flaskflush(self):
		import os
		import sys
		sys.path.append(os.getcwd() + '\plask')
		from appglobal import cb_mothed
		
		if not cb_mothed.has_key(self.id):
			return ""

		sflask = ""
		for key,value in cb_mothed[self.id].iteritems():
			sflask += "@app.route('/" + self.id + "/" + key + "',methods=['POST'])\ndef " + self.id + key + "():\n"
			sflask += "\timport traceback\n\tfrom appglobal import cb_mothed\n\tfrom io import BytesIO\n\timport json\n\tr = {}\n"
			sflask += "\ttry:\n"
			sflask += "\t\tfor cb in cb_mothed[\"" + self.id + "\"][\"" + key + "\"]:\n"
			sflask += "\t\t\tr.update(cb(request.get_json()))\n"
			sflask += "\t\treturn Response(BytesIO(json.dumps(r)), mimetype='text/json')\n"
			sflask += "\texcept:\n"
			sflask += "\t\tfrom log import log\n\t\tlog(traceback.format_exc())\n\n"
			
		return sflask
	