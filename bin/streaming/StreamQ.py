# BlockQueue
from multiprocessing import Queue, Process
import time

class StreamQ:
	def __init__(self,buffer=100):
		self.q = Queue() #use a FIFO queue
		self.BUFFER_SIZE = buffer
	
	def addblock(self,block):
		self.q.put(block)
	
	def nextblock(self,blocking=True):
		return self.q.get(blocking)
	
	# blocking polling method to wait for the queue to fill up
	# TODO refine with condition locks etc
	def buffer(self,BUFFER_SIZE=None):
		if BUFFER_SIZE is None: BUFFER_SIZE = self.BUFFER_SIZE
		n = self.q.qsize()
		
		while (n < BUFFER_SIZE):
			print "Q: testing"
			n = self.q.qsize()
			time.sleep(0.25)
		
		