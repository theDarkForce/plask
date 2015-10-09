# tools
# create at 2015/5/29
# autor: qianqians

def argv_instance(argv, type):
	if not isinstance(argv, type):
		raise "argv need type %"%type
	return argv

def tuple_rbg(t):
	return "RGB(" + str(t[0]) + "," + str(t[1]) + "," + str(t[2]) + ")"

def get_value(key):
	return "value[" + key + "]"	

class jparams(object):
	def __init__(self):
		self.param = "var params = {\"sid\":sid};\n"

	def append(self, key, value):
		self.param += "params[\"" + key + "\"]" + "=" + value + ";\n"

	def get_params(self):
		return self.param

class on_server_response(object):
	def __init__(self):
		self.cb = ""
		self.if_true_cb = ""

	def add_call(self, code):
		self.cb += code

	def add_call_if_true(self, code, key):
		self.if_true_cb += "if (value[\""+ key + "\"]){" + code + "}"

	def add_call_if_false(self, code, key):
		self.if_true_cb += "if (value[\""+ key + "\"] == false){" + code + "}"

	def get_on_server_response(self):
		return "function (requestNumber, value, exception){" + self.cb + self.if_true_cb + "}"

# server callback lambda
# params json dict
# event callback
class server_event(object):
	def __init__(self, event, params, on_server_response_handle):
		self.event = event
		self.params = params
		self.on_server_response_handle = on_server_response_handle
		self.cb = []

	def add_onevent(self, onevent):
		self.cb.append(onevent);

class uievent(object):
	def __init__(self, url, ctrl, uievent):
		self.url = url
		self.ctrl = ctrl
		self.uievent = uievent
		self.onevent = []
		self.server_events = []

	def get_onevent(self):
		js = ""
		for e in self.onevent:
			js += e
		for s in self.server_events:
			js += s.params.get_params() + "\n"
			js += "JSONRequest.post(\"" + self.url + self.ctrl.id + "/" + s.event + "\",\n"
			js += "params,"
			js += s.on_server_response_handle.get_on_server_response() + ");"
		return js

	def add_call_ui(self, code):
		self.onevent.append(code)
	
	def add_server_event(self, sevent):
		self.server_events.append(sevent)