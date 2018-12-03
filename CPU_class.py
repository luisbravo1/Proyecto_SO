from Process import *

class CPU(object):
	def __init__(self, quantum=None,tick=None):
		self.quantum = quantum
		self.quantum_b = quantum
		self.tick = tick
		self.finish = True
		self.process = None

	def run(self):
		if (self.process != None):
			self.quantum -= self.tick
			if (self.quantum <= 0):
				self.quantum = self.quantum_b
				self.finish = True
			print ("Running process..." + self.process)



	def finished(self):
		return (self.finish)

	def add(self,key):
		self.finish = False
		self.process = key