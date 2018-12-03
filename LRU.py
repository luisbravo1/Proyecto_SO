from datetime import datetime
from time import sleep
from Process import *


class LRUCache(object):

	def __init__(self, length, delta=None):
		self.length = length
		self.delta = delta
		self.hash = {}
		self.item_list = []

	def insertItem(self, item):

		if item.key in self.hash:
			# Move the existing item to the head of item_list.
			item_index = self.item_list.index(item)
			self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
			self.item_list.insert(0, item)
		else:
			# Remove the last item if the length of cache exceeds the upper bound.
			if len(self.item_list) > self.length:
				self.removeItem(self.item_list[-1])

			# If this is a new item, just append it to
			# the front of item_list.
			self.hash[item.key] = item
			self.item_list.insert(0, item)

	def getItem(self):
		return self.item_list[0]

	def removeItem(self, item):

		del self.hash[item.key]
		del self.item_list[self.item_list.index(item)]

	def validateItem(self):

		def _outdated_items():
			now = datetime.now()
			for item in self.item_list:
				time_delta = now - item.timestamp
			if time_delta.seconds > self.delta:
				yield item

		map(lambda x: self.removeItem(x), _outdated_items())

	def isEmpty(self):
		return (len(self.item_list) == 0)


def print_cache(cache):
	for i, item in enumerate(cache.item_list):
		print ("index: {0} "
			   "key: {1} "
			   "item: {2} "
			   "timestamp: {3}".format(i,
									   item.key,
									   item.item,
									   item.timestamp))