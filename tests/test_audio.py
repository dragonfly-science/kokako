import unittest

class TestBasicAudio(unittest.TestCase):

    def setUp(self):
        from kokako.score import get_audio
        self.audio = get_audio('tests/files/wind-gust-clipping.wav')

    def test_framerate(self):
        assert self.audio.framerate == 8000
    
    def test_nchannels(self):
        assert self.audio.nchannels == 1
    
    def test_duration(self):
        assert self.audio.duration == 60.0
    
    def test_duration(self):
        assert self.audio.audio.shape[0] == self.audio.duration*self.audio.framerate

    def test_specgram(self):
        self.audio.calculate_specgram(256, 128)
        assert self.audio.specgram.shape == (129, 3749)
