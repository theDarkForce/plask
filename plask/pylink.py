# pylink
# create at 2015/5/28
# autor: qianqians
from tools import argv_instance, tuple_rbg
from pyelement import pyelement

class pylink(pyelement):
	#text-decoration
	NoneDecoration = "none"
	UnderlineDecoration = "underline"

	def __init__(self, link, linkdescribe, cname, layout, praframe, embeddedext = None):
		self.link = link
		self.linkdescribe = linkdescribe

		self.embeddedext = embeddedext

		self.type = "a"

		# when normal
		self.normal_decoration = pylink.NoneDecoration
		self.linkcolor = (0, 0, 0)

		super(self).__init__(cname, layout, praframe)
		
	def flush(self):
		# if img is not none, use img for link, 
		# if img is none, use text for link,
		# this control jump to other page
		# codegen css in page
		shtml = ""
		if self.html is not None:
			shtml = self.html
		else:
			shtml = "<div id=\"" + self.id + "_1\"><a id=\"" + self.id + "\" href=\"" + self.link
			for event, onevent in self.uievent:
				shtml += event + "=" + self.id + event + "(this)"
			shtml += "\"></div>"

		js = ""
		if self.embeddedext is None:
			shtml += self.linkdescribe
		else:
			html,sjs = self.embeddedext.flush()
			js += sjs
			shtml += html
		shtml += "</a>"
		
		if self.js is not None:
			js = self.js
		else:
			for event, onevent in self.uievent.iteritems():
				js += "function " + self.id + event + "(id){"
				for f in onevent:
					js += f
				js += "}\n"
			
		return shtml, js

	def client_set_link(self, link, linkdescribe, decoration, linkcolor):
		js = "id.innerHTML=\"" + linkdescribe + "\";"
		js += "id.href=" + link + ";"
		js += "id.style.color=" + tuple_rbg(linkcolor) + ";"
		js += "id.style.textDecoration=\"" + linkdescribe + "\";"
		return js

	def server_set_link(self, link, linkdescribe, decoration, linkcolor):
		js = "document.getElementById(\"" + self.id + "\").innerHTML=\"" + linkdescribe + "\";"
		js += "document.getElementById(\"" + self.id + "\").href=" + link + ";"
		js += "document.getElementById(\"" + self.id + "\").style.color=" + tuple_rbg(linkcolor) + ";"
		js += "document.getElementById(\"" + self.id + "\").style.textDecoration=\"" + linkdescribe + "\";"
		return js

	def set_normal(self, decoration, link, linkdescribe, linkcolor):
		self.link = link
		self.linkdescribe = linkdescribe
		self.normal_decoration = argv_instance(decoration, int)
		self.linkcolor = argv_instance(linkcolor, tuple)