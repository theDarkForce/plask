# -*- coding: UTF-8 -*-
#  pytext
# create at 2015/9/17
# autor: qianqians
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pypopup(pyelement):
	def __init__(self, cname, width, praframe):
		super(pypopup, self).__init__(cname, pyhtmlstyle.margin_auto, praframe)

		self.divlist = []
		self.width = width

		self.popname = cname

	def client_call(self):
		return "alertWin" + self.id + "(" + str(self.width) + ", value);"

	def server_call(self):
		return "alertWin" + self.id + "(" + str(self.width) + ", {});"

	def close_win(self):
		return "document.body.removeChild(msgObj);\n document.body.removeChild(table);\n"

	def flush(self):
		js = "function alertWin" + self.id + "(width, value){\n"
		js += " var bgcolor = \"RGB(220, 220, 220)\";\n"
		js += " var iWidth = document.documentElement.clientWidth;\n"
		js += " var iHeight = document.documentElement.clientHeight;\n"
		js += " var msgObj=document.createElement(\"div\");\n"
		js += " msgObj.style.position=\"absolute\";\n"
		js += " msgObj.style.top = (((iHeight)/2)-10).toString()+\"px\";\n"
		js += " msgObj.style.left = (((iWidth - width)/2)-10).toString()+\"px\";\n"
		js += " msgObj.style.width = (width+20).toString() + \"px\";\n"
		js += " msgObj.style.borderStyle = \"solid\";\n"
		js += " msgObj.style.borderWidth = \"1px\";\n"
		js += " msgObj.style.borderColor = bgcolor;\n"
		js += " msgObj.style.backgroundColor = bgcolor;\n"
		js += " msgObj.style.filter = \"alpha(opacity=50)\";\n"
		js += " msgObj.style.opacity=\"0.5\";\n"
		js += " var moveX = 0;\n"
		js += " var moveY = 0;\n"
		js += " var moveTop = 0;\n"
		js += " var moveLeft = 0;\n"
		js += " var moveable = false;\n"
		js += " msgObj.onmouseover = function() {\n"
		js += "     msgObj.style.cursor=\"move\";\n"
		js += " };\n"
		js += " msgObj.onmouseout = function(){\n"
		js += "     msgObj.style.cursor=\"auto\";\n"
		js += "     if (moveable) {\n"
		js += "         moveable = false;\n"
		js += "     }\n"
		js += " };\n"
		js += " msgObj.onmousedown = function() {\n"
		js += "     moveable = true;\n"
		js += "     moveX = event.clientX;\n"
		js += "     moveY = event.clientY;\n"
		js += "     moveTop = parseInt(msgObj.style.top);\n"
		js += "     moveLeft = parseInt(msgObj.style.left);\n"
		js += " };\n"
		js += " var table = document.createElement(\"div\");\n"
		js += " msgObj.onmousemove = function() {\n"
		js += "     if (moveable) {\n"
		js += "         var x = moveLeft + event.clientX - moveX;\n"
		js += "         var y = moveTop + event.clientY - moveY;\n"
		js += "         msgObj.style.left = x + \"px\";\n"
		js += "         msgObj.style.top = y + \"px\";\n"
		js += "         table.style.left = (x+10) + \"px\";\n"
		js += "         table.style.top = (y+10) + \"px\";\n"
		js += "     }\n"
		js += " };\n"
		js += " msgObj.onmouseup = function () {\n"
		js += "     if (moveable) {\n"
		js += "         moveable = false;\n"
		js += "         moveX = 0;\n"
		js += "         moveY = 0;\n"
		js += "         moveTop = 0;\n"
		js += "         moveLeft = 0;\n"
		js += "     }\n"
		js += " };\n"
		js += " table.onmouseover = function() {\n"
		js += "     table.style.cursor=\"move\";\n"
		js += " };\n"
		js += " table.onmouseout = function(){\n"
		js += "     table.style.cursor=\"auto\";\n"
		js += "     if (moveable) {\n"
		js += "         moveable = false;\n"
		js += "     }\n"
		js += " };\n"
		js += " table.onmousedown = function() {\n"
		js += "     moveable = true;\n"
		js += "     moveX = event.clientX;\n"
		js += "     moveY = event.clientY;\n"
		js += "     moveTop = parseInt(msgObj.style.top);\n"
		js += "     moveLeft = parseInt(msgObj.style.left);\n"
		js += " };\n"
		js += " table.onmousemove = function() {\n"
		js += "     if (moveable) {\n"
		js += "         var x = moveLeft + event.clientX - moveX;\n"
		js += "         var y = moveTop + event.clientY - moveY;\n"
		js += "         msgObj.style.left = x + \"px\";\n"
		js += "         msgObj.style.top = y + \"px\";\n"
		js += "         table.style.left = (x+10) + \"px\";\n"
		js += "         table.style.top = (y+10) + \"px\";\n"
		js += "     }\n"
		js += " };\n"
		js += " table.onmouseup = function () {\n"
		js += "     if (moveable) {\n"
		js += "         moveable = false;\n"
		js += "         moveX = 0;\n"
		js += "         moveY = 0;\n"
		js += "         moveTop = 0;\n"
		js += "         moveLeft = 0;\n"
		js += "     }\n"
		js += " };\n"
		js += " table.style.borderBottomStyle = \"solid\";\n"
		js += " table.style.borderBottomWidth = \"1px\";\n"
		js += " table.style.borderBottomColor = \"RGB(255, 255, 255)\";\n"
		js += " table.style.borderLeftStyle = \"solid\";\n"
		js += " table.style.borderLeftWidth = \"1px\";\n"
		js += " table.style.borderLeftColor = \"RGB(255, 255, 255)\";\n"
		js += " table.style.borderRightStyle = \"solid\";\n"
		js += " table.style.borderRightWidth = \"1px\";\n"
		js += " table.style.borderRightColor = \"RGB(255, 255, 255)\";\n"
		js += " table.style.borderTopStyle = \"solid\";\n"
		js += " table.style.borderTopWidth = \"1px\";\n"
		js += " table.style.borderTopColor = \"RGB(255, 255, 255)\";\n"
		js += " table.style.backgroundColor = \"RGB(255, 255, 255)\";\n"
		js += " table.style.position=\"absolute\";\n"
		js += " table.style.zIndex=\"1\";\n"
		js += " table.style.top = ((iHeight)/2).toString()+\"px\";\n"
		js += " table.style.left = ((iWidth - width)/2).toString()+\"px\";\n"
		js += " table.style.width = width.toString() + \"px\";\n"
		js += " var table_pop = document.createElement(\"div\");\n"
		js += " table_pop.style.width = width.toString() + \"px\";\n"
		for div in self.divlist:
			js += div.sub()
		js += " table.appendChild(table_pop);\n"
		js += " document.body.appendChild(table);\n"
		js += " msgObj.style.height = (table.offsetHeight +20).toString() + \"px\";\n"
		js += " document.body.appendChild(msgObj);\n"
		js += "}\n"

		return "", js

	def flaskflush(self):
		flask = ""
		for div in self.divlist:
			flask += div.flaskflush()
		return flask