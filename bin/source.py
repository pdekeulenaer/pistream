#source of the stream
from streaming import StreamSender
import audio
import time
import wave


s = StreamSender()
cfg = audio.AudioConfig()
reader = audio.AudioReader(cfg)


while True:
	data = reader.read()
	s.sendblock(data)

reader.terminate()
s.terminate()

