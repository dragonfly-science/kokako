import numpy as np
import struct
from pylab import clf, specgram, savefig, mean, log
from matplotlib import mlab
from matplotlib import pyplot as plt
from datetime import datetime
from contextlib import closing
import wave

class Audio(object):
    def __init__(self, audio, framerate):
        self.audio = audio
        self.framerate = framerate
        self._specgrams = {}
 
    def calculate_specgram(self, nfft, noverlap, **kwargs):
        spec = specgram(self.audio, NFFT=nfft, Fs=self.framerate, noverlap=noverlap, **kwargs)
        self.specgram_nfft = nfft
        self.specgram_overlap = noverlap
        self.specgram = spec[0]
        self.specgram_freqs = spec[1]
        self.specgram_bins = spec[2]
        self.specgram_image = spec[3]
    
    @property
    def nchannels(self):
        try:
            return self.audio.shape[1]
        except IndexError:
            return 1

    @property
    def duration(self):
        return self.audio.shape[0]/self.framerate

def get_audio(filename, offset=0, duration=0):
    with closing(wave.open(filename, 'rb')) as wav:
        wav.rewind()
        framerate = wav.getframerate()
        nchannels = wav.getnchannels()
        if offset:
            offset_frames = int(offset*framerate*nchannels)
            wav.readframes(offset_frames) #Read to the offset in seconds
        if duration:
            nframes = int(duration*framerate*nchannels)
        else:
            nframes = wav.getnframes() - int(offset*framerate*nchannels)
        duration = nframes/float(framerate*nchannels) 
        frames = wav.readframes(nframes)
    return Audio(np.array(struct.unpack_from ("%dh" % (len(frames)/2,), frames)), framerate)

                
class Detector(object):
    """Base class for detectors
    """
    code = None
    version = None
    description = None

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        """Represent the detector as a string"""
        return "%s %s" % (self.code, self.version)

    def score(self, audio):
        """Returns the score as a number"""
        raise NotImplementedError

        

