from multiprocessing.connection import Listener

class StreamReceiver:
	def __init__(self,streamq):
		self.streamq = streamq
		self.run()

	def openconnection(self):
		address = ('localhost',3140)
		print "[INIT] Opening connection on %s)" % str(address)
		self._LISTENER = Listener(address,authkey='1kdw91l')
		self._CONN = self._LISTENER.accept()
		return self._CONN

	def run(self):
		while True:
			try:
				conn = self.openconnection()
				self.serve(conn)
			except EOFError:
				conn.close()
				self._LISTENER.close()
				print "Connection terminated by client"
				

	def serve(self,conn):
		while True:
			msg = conn.recv()
			if msg == 'TERMINATE':
				print 'terminate received'
				self.finalize()
				conn.send("OK")
				conn.close()
				break
			
			resp = self.dispatch(msg)
			conn.send(resp)

	# expects format: {msg:'BLOCK', block:DATA}
	def dispatch(self,msg):
		cmd = msg['msg']
		data = msg['block']
		if cmd == 'BLOCK' :
			self.streamq.addblock(data)
			return 'OK'
		return 'NOK'
		
	def finalize(self):
		pass