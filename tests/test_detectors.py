import unittest

class TestDetectors(unittest.TestCase):

    def setUp(self):
        from kokako.score import get_audio
        from kokako.detectors.kiwi import SimpleKiwi
        from kokako.detectors.intensity import Energy, LowEnergy, Amplitude
        self.score_kiwi = SimpleKiwi()
        self.score_energy = Energy()
        self.score_low_energy = LowEnergy()
        self.score_amplitude = Amplitude()
        self.audio_gust = get_audio('tests/files/wind-gust-clipping.wav')
        self.audio_kiwi = get_audio('tests/files/male-kiwi.wav')

    def test_kiwi(self):
        assert self.score_kiwi.score(self.audio_kiwi) > self.score_kiwi.score(self.audio_gust)
    
    def test_amplitude(self):
        assert self.score_amplitude.score(self.audio_gust) > 32000
    
    def test_amplitude_kiwi(self):
        assert self.score_amplitude.score(self.audio_gust) > self.score_amplitude.score(self.audio_kiwi)
    
    def test_energy(self):
        assert self.score_energy.score(self.audio_gust) > self.score_energy.score(self.audio_kiwi)
    
    def test_low_energy(self):
        assert self.score_low_energy.score(self.audio_gust) > self.score_low_energy.score(self.audio_kiwi)

