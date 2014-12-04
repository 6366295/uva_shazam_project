"""
 TODO
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.io.wavfile as wavfile

samplerate, data = wavfile.read('wav\alcedo_atthis_ijsvogel.wav')

print samplerate

NFFT = 4096

Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(4096*0.5), cmap=plt.cm.gist_rainbow)
plt.show()

spectrum, freqs, t = mlab.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(4096*0.5))

