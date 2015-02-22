#main server file

import streaming
from multiprocessing import Process
import pyaudio
from audio.AudioConfig import AudioConfig
import time


def runserver(streamq):
	rec = streaming.StreamReceiver(streamq)

def runreader(streamq):
	pass
	
	
def run(q):
	serverp = Process(target=runserver, args=(q,))
	serverp.start()

	#readerp = Process(target=runreader, args=(q,))

	# wait for buffer and consume
	print "checking buffer"
	q.buffer(20)
	print "passed buffer test"

	config = AudioConfig()
	p = pyaudio.PyAudio()
	
	
	
	def streamread(in_data,frame_count,time_info,status):
		data = q.nextblock()
		return (data,pyaudio.paContinue)

	print "Setting up stream"
	stream = p.open(format=config.FORMAT, channels=config.CHANNELS,rate=config.RATE,output=True,stream_callback=streamread)
	stream.start_stream()
	
	print "playing?"
	while stream.is_active():
		time.sleep(0.1)
	
	stream.stop_stream()
	stream.close()
	
	print "stream ended"
	
	p.terminate()
	serverp.terminate()

if __name__ == '__main__':
	q = streaming.StreamQ(5)
	run(q)
