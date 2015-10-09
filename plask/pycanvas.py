# pycanvas
# create at 2015/6/15
# autor: qianqians
from tools import argv_instance
from pyelement import pyelement

class pycanvas(pyelement):
	def __init__(self, cname, praframe):
		super(self).__init__(cname, praframe)

		self.type = "canvas"


		
