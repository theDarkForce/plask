# pyborder
# create at 2015/8/27
# autor: qianqians
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pyborder(pyelement):
	center = "center"
	right = "right"
	left = "left"
	top = "top"
	bottom = "bottom"

	def __init__(self, cname, layout, style, praframe):
		self.style = style
		self.size = 0

		self.type = "hr"

		self.border_left_style = pyhtmlstyle.solid
		self.border_right_style = None
		self.border_top_style = None
		self.border_bottom_style = None

		super(pyborder, self).__init__(cname, layout, praframe)

	def flush(self):
		# if img is not none, use img for img,
		# if img is none, use text for img,
		# handle onclick in js and send a requst to service
		# codegen css in page
		shtml = "<div id=\"" + self.id + "_1\" >"
		shtml += "<hr align=" + self.style
		shtml += " width = " + str(self.width)
		if self.color:
			shtml += " color=" + "rgb(" + str(self.color[0]) + "," + str(self.color[1]) + "," + str(self.color[2]) + ")"
		shtml += " size=" + str(self.size) + ">"
		shtml += "</div>"

		return shtml, ""

	def set_size(self, width, height):
		self.width = width
		self.size = height