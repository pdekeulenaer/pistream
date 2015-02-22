import pyaudio

class AudioConfig:
	def __init__(self,BLOCK=4096,FORMAT=pyaudio.paInt32,CHANNELS=2,RATE=44100):
		self.BLOCK = BLOCK
		self.FORMAT = FORMAT
		self.CHANNELS = CHANNELS
		self.RATE = RATE
		self.SAMPLESIZE = pyaudio.get_sample_size(pyaudio.paInt32)