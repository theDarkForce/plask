# pyaudio
# create at 2015/6/12
# autor: qianqians
from pyelement import pyelement

class pyaudio(pyelement):
	def __init__(self, src, cname, layout, praframe):
		self.src = src

		self.type = "audio"

		super(pyaudio, self).__init__(cname, layout, praframe)
		
	def flush(self):
		# codegen css in page
		shtml = ""
		if self.html is not None:
			shtml = self.html
		else:
			index = self.src.rfind("/")
			if index < 0:
				index = self.src.rfind("\\")

			shtml = "<div id=\"" + self.id + "_1\"><audio id=\"" + self.id + "\" src=\"" + self.src
			
			for event, onevent in self.uievent:
				shtml += event + "=" + self.id + event + "(this)"

			shtml += "\" controls=\"controls\">Your browser does not support the audio tag.</audio></div>"

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
			
	def client_set_video(self, src):
		return "id.src = " + src + ";"

	def server_set_audio(self, src):
		return "document.getElementById(\"" + self.id + "\").src = " + src + ";"

	def set_src(self, src):
		self.src = src 