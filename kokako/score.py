import numpy as np
import struct
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

    def score(self, filename, offset=0, duration=0):
        """Returns the score as a tuple of a number and a string. The string
        is formatted as JSON"""
        raise NotImplementedError

    def get_audio(self, filename, offset=0, duration=0):
        """Returns an array with the audio data contained in
            the file file_handle, reading from offset (seconds)
            for duration (seconds).
        """
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
            frames = wav.readframes(nframes)
        return np.array(struct.unpack_from ("%dh" % (len(frames)/2,), frames)), framerate

        

