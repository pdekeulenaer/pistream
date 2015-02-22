import pyaudio
from multiprocessing.connection import Client		
from AudioConfig import AudioConfig


class AudioReader:
	def __init__(self,config=None):
		if config is None: config = AudioConfig()
		self.pa = pyaudio.PyAudio()
		self.config = config
		self.stream = self.pa.open(format=config.FORMAT, channels=config.CHANNELS, rate=config.RATE, input=True, frames_per_buffer=config.BLOCK)		

	def finalize(self):
		self.stream.stop_stream()
		self.stream.close()
		self.pa.terminate()
	
	def read(self,size=None):
		if size is None: size = self.config.BLOCK
		return self.stream.read(size)