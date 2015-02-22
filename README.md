# pistream
# Streaming audio from my laptop to my raspberry pi

This collection of python scripts uses the pyAudio and alsaaudio wrappers on respectively windows and linux to pipe audio from a windows device ('source') to a sound server which can be hosted locally or remotely. My particular usecase uses a Raspberry Pi, where the alsaaudio libraries are used as a wrapper around alsa, to allow for better playback.

Data is streamed over a regular internet connection, using pythons multiprocessing libraries
