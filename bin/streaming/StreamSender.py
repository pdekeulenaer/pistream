from multiprocessing.connection import Client		

class StreamSender:
	def __init__(self,addr=('192.168.0.205',3140),pw='1kdw91l'):
		self.address = addr
		self.pw = pw
		self.conn = self.openconnection(addr,pw)

	def openconnection(self,addr,pw):
		conn = Client(addr,authkey=pw)
		return conn

	def sendblock(self, block):
		msg = {'msg':'BLOCK','block' : block}
		self.conn.send(msg)
		resp = self.conn.recv()
		print resp
	
	def terminate(self):
		self.conn.send('TERMINATE')
		self.conn.close()