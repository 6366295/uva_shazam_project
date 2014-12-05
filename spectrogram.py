"""
 TODO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.io.wavfile as wavfile

samplerate, data = wavfile.read('wav\\alcedo_atthis_ijsvogel.wav')

print samplerate
print data

NFFT = 4096

Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(4096*0.5), cmap=plt.cm.hot)
plt.show()

spectrum, freqs, t = mlab.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(4096*0.5))

a = []

for i in range(0, len(spectrum)):
    a.append(spectrum[i][5])

plt.clf()
plt.ylim([-2,2])
plt.plot(freqs, a)
plt.show()
