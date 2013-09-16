import numpy as np
from matplotlib import mlab
from kokako.score import Detector

class IntensityDetector(Detector):
    code='intensity'
    signal = 'intensity'
    description = 'Average energy from the spectrogram'
    version = '0.1'
    NFFT = 256

    def score(self, filename, offset, duration):
        audio, framrate = self.get_audio(filename, offset, duration)
        clf()
        spec = mlab.specgram(audio, NFFT=self.NFFT, Fs=framerate)
        return (sum(np.min(spec[0][10:, ], 1)),)


class AmplitudeDetector(Detector):
    code='amplitude'
    signal = 'amplitude'
    description = 'Peak amplitude'

    def score(self, filename, offset=0, duration=0):
        audio, framrate = self.get_audio(filename, offset, duration)
        return max(abs(audio))
