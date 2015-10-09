# pyhtmlstyle
# create at 2015/5/28
# autor: qianqians
from tools import argv_instance

class pyhtmlstyle(object):
	idregister = []

	# margin
	margin_left = 0
	margin_right = 1
	margin_top = 2
	margin_bottom = 3
	margin_auto = 4

	float_left = " float:left;"
	float_right = " float:right;"
	float_new_line = ""

	# border
	outset = "outset"
	solid = "solid"
	dotted = "dotted"
	dashed = "dashed"
	double = "double"
	none = "none"

	#text-decoration
	NoneDecoration = "none"
	UnderlineDecoration = "underline"
	OverlineDecoration = "overline"
	LineThroughDecoration = "line-through"
	BlinkDecoration = "blink"

	#cursor
	url = "url"
	default = "default"
	auto = "auto"
	crosshair = "crosshair"
	pointer = "pointer"
	move = "move"
	e_resize = "e-resize"
	ne_resize = "ne-resize"
	nw_resize = "nw-resize"
	n_resize = "n-resize"
	se_resize = "se-resize"
	sw_resize = "sw-resize"
	s_resize = "s-resize"
	w_resize = "w-resize"
	text = "text"
	wait = "wait"
	help_ = "help"

	def __init__(self, cname, layout):
		# register id
		if cname in pyhtmlstyle.idregister:
			raise "dup id for contorl"
		pyhtmlstyle.idregister.append(cname)
		self.id = cname

		#cursor
		self.cursor = None

		#layout
		self.left = -1
		self.top = -1
		self.right = -1
		self.bottom = -1

		#size
		self.width = -1
		self.height = -1

		#border
		self.border_style = None
		self.border_size = 0
		self.border_color = None

		self.border_left_style = None
		self.border_right_style = None
		self.border_top_style = None
		self.border_bottom_style = None

		#visibility
		self.visibility = True

		# css
		self.margin = layout

		# html
		self.css = None
		self.html = None
		self.js = None

		#color
		self.color = None

		#font
		self.font_size = None
		self.font_color = None

		#background-color
		self.background_color = None

		#decoration
		self.normal_decoration = None

		#newline
		self.clear = None

	def extended(self, html = None, css = None, js = None):
		self.html = html
		self.css = css
		self.js = js

	def cssstyle(self):
		if self.css is not None:
			return self.css

		scss = "div#" + self.id + "_1{"
		if self.width > 0:
			scss += "width:" + str(self.width) + "px;"
		if self.height > 0:
			scss +=  " height:" + str(self.height) + "px;"

		if self.border_style:
			scss +=  " border-style:" + self.border_style + "; border-width: " + str(self.border_size) + "px;"

		if self.border_color:
			scss +=  " border-color:rgb(" + str(self.border_color[0]) + "," + str(self.border_color[1]) + "," + str(self.border_color[2]) + ");"

		if self.border_left_style is not None:
			scss += " border-left-style:" + self.border_left_style + "; border-width: " + str(self.border_size) + "px;"

		if self.border_right_style is not None:
			scss += " border-right-style:" + self.border_right_style + "; border-width: " + str(self.border_size) + "px;"

		if self.border_top_style is not None:
			scss += " border-top-style:" + self.border_top_style + "; border-width: " + str(self.border_size) + "px;"

		if self.border_bottom_style is not None:
			scss += " border-bottom-style:" + self.border_bottom_style + "; border-width: " + str(self.border_size) + "px;"

		if self.visibility:
			scss +=  " visibility:visible;"
		else:
			scss +=  " visibility:hidden;"

		if self.font_size:
			scss += " font-size:" + str(self.font_size) + "%;"

		if self.font_color:
			scss += " color:rgb(" + str(self.font_color[0]) + "," + str(self.font_color[1]) + "," + str(self.font_color[2]) + ");"

		if self.background_color:
			scss += " background-color:rgb(" + str(self.background_color[0]) + "," + str(self.background_color[1]) + "," + str(self.background_color[2]) + ");"

		if self.normal_decoration:
			scss += " text-decoration:" + self.normal_decoration

		if self.clear:
			scss += " clear:both; "

		return scss

	def csslayout(self):
		scss = ""
		if self.margin == pyhtmlstyle.float_left or self.margin == pyhtmlstyle.float_right or self.margin == pyhtmlstyle.float_new_line:
			scss += self.margin

		isset = False
		left = "auto"
		right = "auto"
		top = "auto"
		bottom = "auto"
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
			scss += " margin: " + top + " " + right + " " + bottom + " " + left + ";"
		elif self.margin is pyhtmlstyle.margin_left:
			scss += " margin:auto auto auto 0px;"
		elif self.margin is pyhtmlstyle.margin_right:
			scss += " margin:auto 0px auto auto;"
		elif self.margin is pyhtmlstyle.margin_top:
			scss += " margin:0px auto auto auto;"
		elif self.margin is pyhtmlstyle.margin_bottom:
			scss += " margin:auto auto 0px auto;"
		elif self.margin is pyhtmlstyle.margin_auto:
			scss += " margin:auto auto auto auto;"

		return scss

	def set_newline(self):
		self.clear = "both"

	def gencss(self):
		return self.cssstyle() + self.csslayout() + "}"

	def set_border_style(self, style):
		self.border_style = style

	def set_border_size(self, size):
		self.border_size = size

	def set_border_color(self, color):
		self.border_color = color

	def set_visibility(self, isvisibility):
		self.visibility = isvisibility

	def client_set_size(self, width, height):
		js = "id.style.width=" + str(width) + ";"
		js += "id.style.height=" + str(height) + ";"
		return js

	def server_set_size(self, width, height):
		js = "document.getElementById(\"" + self.id + "\").style.width=" + str(width) + ";"
		js += "document.getElementById(\"" + self.id + "\").style.height=" + str(height) + ";"
		return js

	def set_font_size(self, size):
		self.font_size = size

	def client_set_font_size(self, size):
		js = "id.style.font_size=" + str(size) + "%;"
		return js

	def server_set_font_size(self, size):
		js = "document.getElementById(\"" + self.id + "\").style.font_size=" + str(size) + "%;"
		return js

	def client_set_font_color(self, color):
		js = "id.style.color=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def server_set_font_color(self, color):
		js = "document.getElementById(\"" + self.id + "\").style.color=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def set_background_color(self, color):
		self.background_color = color

	def client_set_background_color(self, color):
		js = "id.style.backgroundColor=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def server_set_background_color(self, color):
		js = "document.getElementById(\"" + self.id + "\").style.backgroundColor=\"rgb(" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + ")\";"
		return js

	def pop_set_cursor(self, cursor):
		js = "table_" + self.id + ".style.cursor=\"" + cursor + "\";"
		return js

	def client_set_cursor(self, cursor):
		js = "id.style.cursor=\"" + cursor + "\";"
		return js

	def server_set_cursor(self, cursor):
		js = "document.getElementById(\"" + self.id + "\").style.cursor=\"" + cursor + "\";"
		return js

	def set_margin_style(self, margin):
		self.margin = margin

	def set_left_border_style(self, style):
		self.border_left_style = style

	def set_right_border_style(self, style):
		self.border_right_style = style

	def set_top_border_style(self, style):
		self.border_top_style = style

	def set_bottom_border_style(self, style):
		self.border_bottom_style = style

	def set_size(self, width, height):
		self.width = width
		self.height = height

	def set_location(self, left = -1, top = -1):
		if left >= 0:
			self.left = left
		if top >= 0:
			self.top = top
			if self.height < 0:
				self.height = 0