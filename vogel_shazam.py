import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.io.wavfile as wavfile

from peakdetect import peakdet

def all_peaks(spectrum, freqs, t, threshold):
    peak_list = []
    peak_array = []
    
    for i in range(len(t)):
        maxtab, mintab = peakdet(spectrum[:,i],.3, threshold)

        for j in maxtab:
            peak_list.append(tuple((t[i] , freqs[int(j[0])])))
            peak_array.append([t[i] , freqs[int(j[0])]])
    return peak_list, np.array(peak_array)

    #plt.plot(spectrum[:,0])
    #plt.scatter(np.array(maxtab)[:,0], np.array(maxtab)[:,1], color='blue')
    #plt.show()

def plot_peaks(peak_array, NFFT, samplerate):
    Pxx, freqs, bins, im = plt.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(NFFT*0.5), cmap=plt.cm.hot)

    plt.scatter(peak_array[:,0], peak_array[:,1], color='blue')
    plt.show()
    

if __name__=="__main__":
    samplerate, data = wavfile.read('wav\\corvus_monedula_kauw.wav')
    
    NFFT = 4096

    print 'samplerate: ' + str(samplerate)

    spectrum, freqs, t = mlab.specgram(data, NFFT=NFFT, Fs=samplerate, noverlap=int(NFFT*0.5))

    peak_list, peak_array = all_peaks(spectrum, freqs, t, 500)

    plot_peaks(peak_array, NFFT, samplerate)
    
    
