import numpy as np
from pylab import clf, specgram, mean, log
from matplotlib import mlab
from datetime import datetime
from kokako.score import Detector
import json

class SimpleKiwiDetector(Detector):
    code='simple-kiwi'
    signal = 'kiwi'
    description = 'Simple detector for north-island brown kiwi, based on energy between 1600 and 2200 Hz'
    version = '0.1.1'
    window = 0.032
    lower_call_frequency = 1600
    upper_call_frequency = 2200
    lower_syllable_frequency = 0.5
    upper_syllable_frequency = 1.1

    def score(self, filename, duration=0, framerate=0):
        audio, framerate = self.get_audio(filename, duration=0, framerate=0)
        NFFT = int(self.window*framerate)
        clf()
        spec = mlab.specgram(audio, NFFT=NFFT, noverlap=NFFT/2, Fs=framerate)
        freqs = np.where((spec[1] >= self.lower_call_frequency)*(spec[1] <= self.upper_call_frequency))
        spec2 = mlab.specgram(mean(log(spec[0][freqs[0],]), 0), NFFT=1024, noverlap=512, Fs=2/self.window)
        freqs2 = np.where((spec2[1] >= self.lower_syllable_frequency)*(spec2[1] <= self.upper_syllable_frequency))
        max_kiwi = max(np.max(spec2[0][freqs2[0],:], 0))
        mean_kiwi = np.exp(np.mean(np.mean(np.log(spec2[0][freqs2[0], :]), 0)))
        return json.dumps({'score': max_kiwi/mean_kiwi})

