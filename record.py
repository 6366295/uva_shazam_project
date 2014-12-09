import pyaudio
import sys
import wave as wv

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                output=True,
                frames_per_buffer=chunk)

frames = []

print "* recording"
for i in range(0, 44100 / chunk * RECORD_SECONDS):
    data = stream.read(chunk)
    frames.append(data)
    # check for silence here by comparing the level with 0 (or some threshold) for 
    # the contents of data.
    # then write data or not to a file

print "* done"

stream.stop_stream()
stream.close()
p.terminate()

wave_file = wv.open('test.wav', 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(pyaudio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()
