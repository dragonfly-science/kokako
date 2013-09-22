import numpy as np
from kokako.score import Detector

class Energy(Detector):
    code = 'energy-above-200'
    description = 'Energy of the minimum spectrogram, above 200 Hz'
    version = '0.1'
    window = 0.032
    lower_frequency = 200

    def score(self, audio):
        nfft = int(self.window*audio.framerate)
        audio.calculate_specgram(nfft=nfft, noverlap=nfft/2)
        freqs = np.where(audio.specgram_freqs >= self.lower_frequency)[0]
        return sum(np.min(audio.specgram[freqs, ], 1))*(audio.specgram_freqs[1] - audio.specgram_freqs[0])


class LowEnergy(Detector):
    code = 'energy-below-1000'
    description = 'Energy of the minimum spectrogram, below 1 kHz'
    version = '0.1'
    window = 0.032
    upper_frequency = 1000

    def score(self, audio):
        nfft = int(self.window*audio.framerate)
        audio.calculate_specgram(nfft=nfft, noverlap=nfft/2)
        freqs = np.where(audio.specgram_freqs <= self.upper_frequency)[0]
        return sum(np.min(audio.specgram[freqs, ], 1))*(audio.specgram_freqs[1] - audio.specgram_freqs[0])


class Amplitude(Detector):
    code = 'amplitude'
    description = 'Peak amplitude'
    version = '0.1'

    def score(self, audio):
        return max(abs(audio.audio))
