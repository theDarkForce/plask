# pycanvas
# create at 2015/6/15
# autor: qianqians
from tools import argv_instance
from pyelement import pyelement
from pyhtmlstyle import pyhtmlstyle

class pycanvas(pyelement):
	def __init__(self, cname, praframe):
		super(self).__init__(cname, praframe)

		self.type = "canvas"

	def defflush(self):
			js = "var rotateangle = 0;\n"
			js += "var rotatex = 0;\n"
			js += "var rotatey = 0;\n"
			js += "function rotate(x, y, angle){\n"
			js += " rotatex = x;\n"
			js += " rotatey = y;\n"
			js += " rotateangle = angle;\n"
			js += "}\n"
			js += "function drawimage(img, rangex, rangey, rangew, rangeh, locationx, locationy, locationw, locationh, maskr, maskg, maskb, alpha){\n"
			js += " var img = document.getElementById(img);\n"
			js += " var cc = document.createElement(\"canvas\");\n"
			js += " var cctx =cc.getContext(\"2d\");\n"
			js += " cctx.drawImage(img, 0, 0);\n"
			js += " var drawimgdata = cctx.getImageData(0, 0, cc.width, cc.height);\n"
			js += " for(var i = locationx; i < imgData.width; i++){\n"
			js += "     for(var j = locationy; j < imgData.height; j++){\n"
			js += "         var cx = (rangex+(i-locationx)*rangew/locationw);\n"
			js += "         var cy = (rangey+(j-locationy)*rangeh/locationh);\n"
			js += "         var girth = Math.sqrt((cx-rotatex)*(cx-rotatex) + (cy-rotatey)*(cy-rotatey));\n"
			js += "         var cx = (cx-rotatex)*Math.cos(rotateangle)-(cy-rotatey)*Math.sin(rotateangle)+rotatex;\n"
			js += "         var cy = (cx-rotatex)*Math.sin(rotateangle)+(cy-rotatey)*Math.cos(rotateangle)+rotatey;\n"
			js += "         var index=cx+cy*drawimgdata.width;\n"
			js += "         var index1 = i+j*imgData.width;\n"
			js += "         var r = drawimgdata[index];\n"
			js += "         if(r != maskr){\n"
			js += "             imgData[index1] = r;"
			js += "         }else{\n"
			js += "             imgData[index1] = imgData[index]*(1-alpha) + r*alpha;"
			js += "         }\n"
			js += "         var g = drawimgdata[index+1];\n"
			js += "         if(g != maskg){\n"
			js += "             imgData[index1+1] = g;"
			js += "         }else{\n"
			js += "             imgData[index1+1] = imgData[index+1]*(1-alpha) + r*alpha;"
			js += "         }\n"
			js += "         var b = drawimgdata[index+2];\n"
			js += "         if(b != maskb){\n"
			js += "             imgData[index1+2] = b;"
			js += "         }else{\n"
			js += "             imgData[index1+2] = imgData[index+2]*(1-alpha) + r*alpha;"
			js += "         }\n"
			js += "     }\n"
			js += " }\n"
			js += "}\n"

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
			shtml = "<div id=\"" + self.id + "_1\"><canvas " + "id=\"" + self.id + "\""
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
			shtml += " /></div>"

		js = ""
		if self.js is not None:
			js = self.js
		else:
			js += "var c" + self.id + "=document.getElementById(\"" + self.id + "\");\n"
			js += "var ctx" + self.id + "=c.getContext(\"2d\");\n"
			js += "var imgData" + self.id + "=ctx.createImageData(" + str(self.width) + "," + str(self.height) + ");\n"

			for event, onevent in self.uievent.iteritems():
				js += "function " + self.id + event + "(id){"
				for f in onevent:
					js += f
				js += "}\n"

		return shtml, js

	def drawimage(self, img, range , location, mask, alpha):
		return " drawimage(\""+img.id+"\","+str(range[0])+","+str(range[1])+","+str(range[2])+","+str(range[3])+","+str(location[0])+","+str(location[1])+","+str(location[2])+","+str(location[3])+","+str(mask[0])+","+str(mask[1])+","+str(mask[2])+","+str(alpha)+");\n"

	def make_current(self):
		return "ctx.putImageData(imgdata, 0, 0);"