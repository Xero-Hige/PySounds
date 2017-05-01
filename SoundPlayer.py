import math
from threading import Thread

from pyaudio import *

SPACING = 2  # Space between two sounds

DEFAULT_WIDTH = 1  # 8bits
SAMPLE_RATE = 22050


class Sound(object):
    def __init__(self, frequency, function, volume=0.2):
        self.frequency = frequency
        self.volume = volume
        self.function = function

    def _get_samples(self, duration=1):
        n_samples = int(SAMPLE_RATE * duration)

        samples = (int(self.function(t) * 0x7f + 0x80) for t in range(n_samples))

        return bytes(bytearray(samples)) + b'\x80' * SPACING


class SoundFactory(object):
    @staticmethod
    def get_sine_sound(frequency, volume):
        return Sound(frequency,
                     lambda t: volume * math.sin(2 * math.pi * frequency * t / SAMPLE_RATE),
                     volume)

class SoundPlayer(object):
    def __init__(self, number_of_channels, width=DEFAULT_WIDTH):
        p = PyAudio()

        self.channels = [p.open(format=p.get_format_from_width(width),
                                channels=1,  # mono
                                rate=SAMPLE_RATE,
                                output=True) for _ in range(number_of_channels)]

        self.number_of_channels = number_of_channels

    def get_sample_rate(self):
        return SAMPLE_RATE

    def play_sounds(self, sound_list, duration=1):
        samples = [sound._get_samples(duration) for sound in sound_list]

        threads = [
            Thread(target=self.channels[i].write, args=(samples[i],))
            for i in range(min(len(samples), self.number_of_channels))]

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    def play_song(self, sounds_list):
        samples = [b'\x80' for _ in range(self.number_of_channels)]
        for time_slice in sounds_list:
            for i, sound in enumerate(time_slice[0]):
                samples[i] += sound._get_samples(time_slice[1])

        threads = [
            Thread(target=self.channels[i].write, args=(samples[i],))
            for i in range(min(len(samples), self.number_of_channels))]

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    def close(self):
        for stream in self.channels:
            stream.stop_stream()
            stream.close()
