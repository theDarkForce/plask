# tools
# create at 2015/5/29
# autor: qianqians

def sys_log_handle(log):
	print log

log_file = "log.txt"
def set_log_file(path):
	log_file = path

def file_log_handle(log):
	file = open(log_file, "a")
	file.write(log)
	file.close()

mongodb_ip = "127.0.0.1"
mongodb_port = 27017
mongodb_db = "plask"
mongodb_collection = "log"
def set_log_db(db, collection):
	mongodb_db = db
	mongodb_collection = collection

def db_log_handle(log):
	import pymongo
	connection=pymongo.Connection(mongodb_ip, mongodb_port)
	db = connection[mongodb_db]
	collection = db[mongodb_collection]
	collection.insert({"log":log})

sys = sys_log_handle
file = file_log_handle
mongo_db = db_log_handle

log_handle = sys
def set_log_handle(handle):
	log_handle = handle

def log(logdata):
	log_handle(logdata)
