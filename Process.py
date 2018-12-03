from datetime import datetime

class Process(object):

	def __init__(self, key, item, mem):
		self.key = key
		self.mem = mem
		self.timestamp = datetime.now()
		self.item = item