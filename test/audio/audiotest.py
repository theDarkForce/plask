# buttontest
# create at 2015/6/15
# autor: qianqians
import sys
sys.path.append('../../')
from plask import pyaudio, pypage, plaskapp, pyhtmlstyle, pyfile, uievent

def test():
	app = plaskapp('0.0.0.0', 5000)


	p = pypage('audiotest', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_left)
	p.add_page_route('/')
	file = open('./res/normal_way.mp3', 'rb')
	f = pyfile(file.read(), 'normal_way.mp3', p)
	file.close()
	b = pyaudio(f.url(), 'audio', pyhtmlstyle.margin_left, p)

	p.init()

	app.run()

if __name__ == '__main__':
	test()
