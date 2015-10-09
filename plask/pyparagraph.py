# paragraph
# create at 2015/5/28
# autor: qianqians
from tools import argv_instance, tuple_rbg
from pyelement import pyelement

class pyparagraph(pyelement):
	#font-style
	fontStyleNormal = 0
	fontStyleItalic = 1
	fontStyleOblique = 2

	#font-family
	fontSerif = 0
	fontSansserif = 1
	fontMonospace  = 2
	fontCursive = 3
	fontFantasy = 4

	#event onkeypress && key == enter
	onkeypressenter = 0

	def __init__(self, normal_text, cname, layout, praframe):
		# when normal
		self.normal_text = normal_text
		self.normal_backcolor = (255, 255, 255)
		self.normal_fontcolor = (0, 0, 0)
		self.normal_font_size = 40
		self.normal_font_weight = 400
		self.normal_font_style = pyparagraph.fontStyleNormal
		self.normal_font_family = pyparagraph.fontSerif
		self.type = "p"

		super(pyparagraph, self).__init__(cname, layout, praframe)
		
	def flush(self):
		# if img is not none, use img for text, 
		# if img is none, use text for text,
		# handle onclick in js and send a requst to service
		# codegen css in page
		shtml = ""
		if self.html is not None:
			shtml = self.html
		else:
			shtml = "<div id=\"" + self.id + "_1\"><p id=\"" + self.id + "\""

			for event, onevent in self.uievent:
				shtml += event + "=" + self.id + event + "(this)"

			shtml += ">" + self.normal_text + "</p></div>"
		
		js = ""
		if self.js is not None:
			js = self.js
		else:
			for event, onevent in self.uievent.iteritems():
				js += "function " + self.id + event + "(id){" + onevent + "}\n"
		
		return shtml, js

	def client_set_text(self, text, textcolor, backcolor):
		js = "id.innerHTML=\"" + text + "\";\n"
		js += "id.style.color=" + tuple_rbg(textcolor) + ";\n"
		js += "id.style.backgroundColor=" + tuple_rbg(backcolor) + ";\n"
		return js

	def server_set_text(self, text_key, textcolor_key, backcolor_key):
		js = "document.getElementById(\"" + self.id + "\").innerHTML=value[\"" + text_key + "\"];"
		js += "document.getElementById(\"" + self.id + "\").style.color=value[\"" + textcolor_key + "\"];"
		js += "document.getElementById(\"" + self.id + "\").style.backgroundColor=value[\"" + backcolor_key + "\"];"
		return js

	def server_set_text_simplate(self, text):
		js = "document.getElementById(\"" + self.id + "\").innerHTML=\"" + text + "\";"
		return js

	def set_normal_style(self, backcolor = None, fontcolor = None, decoration = None, font_size = None, font_weight = None, font_style = None, font_family = None):
		self.normal_backcolor = argv_instance(backcolor, tuple)
		self.normal_fontcolor = argv_instance(fontcolor, tuple)
		self.normal_decoration = argv_instance(decoration, int)
		self.normal_font_size = argv_instance(font_size, int)
		self.normal_font_weight = argv_instance(font_weight, int)
		self.normal_font_style = argv_instance(font_style, int)
		self.normal_font_family = argv_instance(font_family, int)
		