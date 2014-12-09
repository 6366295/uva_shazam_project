import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.io.wavfile as wavfile

import re
import glob
import hashlib

from peakdetect import peakdet
from fingerprinting import generate_fingerprints


def all_peaks(spectrum, freqs, t, threshold):
    peak_list = []
    peak_array = []
    
    for i in range(len(t)):
        maxtab, mintab = peakdet(spectrum[:,i],.3, threshold)

        for j in maxtab:
            peak_list.append(tuple((t[i] , freqs[int(j[0])])))
            peak_array.append([t[i] , freqs[int(j[0])]])
            
    return peak_list, np.array(peak_array)


def plot_peaks(peak_array, NFFT, samplerate):
    Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(NFFT*0.5), cmap=plt.cm.hot)

    plt.scatter(peak_array[:,0], peak_array[:,1], color='blue')
    plt.show()


def stereo_to_mono(data):
    return (data[:,0] + data[:,1])/2.0

def analyze(file):
    samplerate, data = wavfile.read(file)

    if len(data.shape) == 2:
        data = stereo_to_mono(data)

    NFFT = 4096

    #print 'samplerate: ' + str(samplerate)

    spectrum, freqs, t = mlab.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(NFFT*0.5))

    peak_list, peak_array = all_peaks(spectrum, freqs, t, 500)

    #plot_peaks(peak_array, NFFT, samplerate)

    return generate_fingerprints(peak_list)

def create_database():
    for file in glob.glob('wav\\*.wav'):
        print file
        fingerprints = analyze(file)

        file_obj = open('database\\' + re.findall('wav\\\\(.*?)\.wav', file)[0] + '.txt', 'w')
        for i in range(len(fingerprints)):
            file_obj.write(str(fingerprints[i][0]) + ',' + str(fingerprints[i][1]) + '\n')
        file_obj.close()


def read_database():
    database_list = {}
    
    for file in glob.glob('database\\*.txt'):
        file_obj = open(file)
        filename = re.findall('database\\\\(.*?)\.txt', file)[0]
        database_list[filename] = []
        for line in file_obj.readlines():
            temp = re.split(',', line)
            temp[1] = re.sub('\n', '', temp[1])
            database_list[filename].append(tuple((float(temp[0]), temp[1])))

    return database_list
