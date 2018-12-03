from Process import *

class CPU(object):
	process = None
	def __init__(self, quantum=None,tick=None):
		self.quantum = quantum
		self.quantum_b = quantum
		self.tick = tick
		self.finish = True

	def add(self,key):
		self.finish = False
		self.process = key

	def run(self):
		if (not self.process == None):
			self.quantum -= self.tick
			if (self.quantum <= 0):
				self.quantum = self.quantum_b
				self.finish = True

	def quantum_end(self):
		self.process = None
		self.finish = True


	def finished(self):
		return (self.finish)
