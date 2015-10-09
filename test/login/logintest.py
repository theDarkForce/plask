# buttontest
# create at 2015/6/15
# autor: qianqians
import sys
sys.path.append('../../')
from plask import *
import json

def test():
	app = plaskapp('0.0.0.0', 5000)

	p = pypage('edittest', 'http://127.0.0.1:5000/', pyhtmlstyle.margin_left)
	p.add_page_route('/')
	e = pyedit('edit', pyedit.text, pyhtmlstyle.margin_left, p)
	b = pybutton('button', 'button', pyhtmlstyle.margin_left, p)

	e.set_location(0, 1)
	b.set_location(180, 0)

	t = pyparagraph('text', "text", pyhtmlstyle.margin_auto, p)
	t.set_location(0, 0)
	t.set_visibility(False)

	ev = uievent('http://127.0.0.1:5000/', b, pyelement.onclick)
	params = jparams()
	params.append("input", e.client_get_input_text())
	onsev = on_server_response()
	onsev.add_call(e.server_get_input_text("output"))
	onsev.add_call(e.server_set_visible(False))
	onsev.add_call(b.server_set_visible(False))
	onsev.add_call(t.server_set_visible(True))
	onsev.add_call(t.server_set_text_simplate("456"))
	sev = server_event("submit", params, onsev)
	def on_click(p):
		return {"output":"456"}
	sev.add_onevent(on_click)
	ev.add_server_event(sev)
	b.register_uievent(ev)

	p.init()

	app.run()

if __name__ == '__main__':
	test()
