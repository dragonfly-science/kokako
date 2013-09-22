import numpy as np
from pylab import mean, log
from matplotlib import mlab
from kokako.score import Detector

class SimpleKiwi(Detector):
    code = 'simple-north-island-brown-kiwi'
    description = 'Simple detector for north-island brown kiwi, based on energy between 1600 and 2200 Hz'
    version = '0.1.2'
    window = 0.032
    lower_call_frequency = 1600
    upper_call_frequency = 2200
    lower_syllable_frequency = 0.5
    upper_syllable_frequency = 1.1

    def score(self, audio):
        nfft = int(self.window*audio.framerate)
        audio.calculate_specgram(nfft=nfft, noverlap=nfft/2)
        freqs = np.where((audio.specgram_freqs >= self.lower_call_frequency)*(audio.specgram_freqs <= self.upper_call_frequency))
        spec2 = mlab.specgram(mean(log(audio.specgram[freqs[0],]), 0), NFFT=1024, noverlap=512, Fs=2/self.window)
        freqs2 = np.where((spec2[1] >= self.lower_syllable_frequency)*(spec2[1] <= self.upper_syllable_frequency))
        max_kiwi = max(np.max(spec2[0][freqs2[0], :], 0))
        mean_kiwi = np.exp(np.mean(np.mean(np.log(spec2[0][freqs2[0], :]), 0)))
        return max_kiwi/mean_kiwi

