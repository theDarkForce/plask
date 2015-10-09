# buttontest
# create at 2015/6/15
# autor: qianqians
import sys
sys.path.append('../../')
from plask import pyvideo, pypage, plaskapp, pyhtmlstyle, pyfile, uievent

def test():
	app = plaskapp('0.0.0.0', 5000)


	p = pypage('videotest', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_left)
	p.add_page_route('/')
	file = open('./res/xpg.mp4', 'rb')
	f = pyfile(file.read(), 'xpg.mp4', p)
	file.close()
	b = pyvideo(f.url(), 'video', pyhtmlstyle.margin_left, p)

	p.init()

	app.run()

if __name__ == '__main__':
	test()
