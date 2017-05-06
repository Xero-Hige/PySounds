import math
import random
from threading import Thread

from pyaudio import *

SPACING = 10  # Space between two sounds

DEFAULT_WIDTH = 1  # 8bits
SAMPLE_RATE = 22050


class Sound(object):
    def __init__(self, frequency, wave_function):
        self.frequency = frequency
        self.function = wave_function

    def _get_samples(self, duration=1):
        n_samples = int(SAMPLE_RATE * duration)

        samples = (int(self.function(t) * 0x7f + 0x80) for t in range(n_samples))

        return bytes(bytearray(samples)) + b'\x80' * SPACING


class SoundFactory(object):
    @staticmethod
    def square_wave(t, sample_rate, frequency, duty_cycle=0.5):
        dt = ((t * frequency) % sample_rate) / sample_rate
        if dt > duty_cycle:
            return -1
        return 1

    @staticmethod
    def triangular_wave(t, sample_rate, frequency):
        dt = ((t * frequency) % sample_rate) / sample_rate
        if dt <= 0.25:
            return dt * 4

        if 0.25 < dt <= 0.75:
            return 1 - ((dt - 0.25) * 4)

        return (dt - 0.75) * 4 - 1

    @staticmethod
    def get_square_sound(frequency, volume, duty_cycle=0.5):
        return Sound(frequency,
                     lambda t: volume * SoundFactory.square_wave(t, SAMPLE_RATE, frequency, duty_cycle))

    @staticmethod
    def get_triangular_sound(frequency, volume):
        return Sound(frequency,
                     lambda t: volume * SoundFactory.triangular_wave(t, SAMPLE_RATE, frequency))

    @staticmethod
    def get_sine_sound(frequency, volume):
        return Sound(frequency,
                     lambda t: volume * math.sin(2 * math.pi * frequency * t / SAMPLE_RATE))

    @staticmethod
    def get_noise_sound(frequency, volume):
        return Sound(frequency,
                     lambda t: volume * random.choice([-1, 1]))


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
