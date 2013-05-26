import numpy as np
from pylab import clf, specgram, savefig, mean, log
from matplotlib import mlab
from matplotlib import pyplot as plt
from datetime import datetime
from contextlib import closing
import wave


class Detector(object):
    """Base class for detectors
    """
    code = None
    signal = None
    version = None
    description = None

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        """Represent the detector as a string"""
        return "%s %s" % (self.code, self.version)

    def score(self, audio):
        """Returns the score as a tuple of a number and a string. The string
        is formatted as JSON"""
        raise NotImplementedError

    def get_audio(self, file_handle, offset=0, duration=60):
        """Returns an array with the audio data contained in
            the file file_handle, reading from offset (seconds)
            for duration (seconds).
        """
        with closing(wave.open(file_handle, 'r')) as wav:
            wav.rewind()
            if offset:
                wav.readframes(int(offset*self.sample_rate*self.nchannels)) #Read to the offset in seconds
            if not duration:
                duration = self.duration - offset
            frames = wav.readframes(int(duration*self.sample_rate*self.nchannels))
            framrate = wav.getframerate()
        return np.array(struct.unpack_from ("%dh" % (len(frames)/2,), frames)), framerate

        

