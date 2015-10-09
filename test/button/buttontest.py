# buttontest
# create at 2015/6/15
# autor: qianqians
import sys
sys.path.append('../../')
from plask import pybutton, pypage, plaskapp, pyhtmlstyle, uievent

def test():
	app = plaskapp('0.0.0.0', 5000)

	p = pypage('buttontest', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_left)
	p.add_page_route('/')
	b = pybutton('button', 'button', pyhtmlstyle.margin_left, p)

	#uievent event
	#b.register_uievent()

	p.init()

	app.run()

if __name__ == '__main__':
	test()
