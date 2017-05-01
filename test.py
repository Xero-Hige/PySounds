#!/usr/bin/python3
import SoundPlayer

sp = SoundPlayer.SoundPlayer(2)
A = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 0, 0.1)
Bb = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 1, 0.1)
B = SoundPlayer.SoundFactory.get_sine_sound(493.88, 0.1)
C = SoundPlayer.SoundFactory.get_sine_sound(523.25, 0.1)
Db = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 4, 0.1)
D = SoundPlayer.SoundFactory.get_sine_sound(587.33, 0.1)
Eb = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 6, 0.1)
E = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 7, 0.1)
F = SoundPlayer.SoundFactory.get_sine_sound(698.46, 0.1)
Gb = SoundPlayer.SoundFactory.get_sine_sound(440 * (2 ** (1 / 12)) ** 9, 0.1)
G = SoundPlayer.SoundFactory.get_sine_sound(783.99, 0.1)
Ab = SoundPlayer.SoundFactory.get_sine_sound(830.61, 0.1)
AM = SoundPlayer.SoundFactory.get_sine_sound(880.00, 0.1)
Gm = SoundPlayer.SoundFactory.get_sine_sound(392.00, 0.1)

Em = SoundPlayer.SoundFactory.get_sine_sound(329.63			, 0.1)

""" A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 12, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 13, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 14, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 15, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 16, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 17, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 18, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 19, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 20, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 21, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 22, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 23, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 24, 0.5)
A = SoundPlayer.SoundFactory.get_sine_sound(220*(2 **(1/12)) ** 25, 0.5) """

tempo = 0.15
sp.play_sounds([E,B], 4 * tempo)
sp.play_sounds([B,Gm], 2 * tempo)
sp.play_sounds([A,C], 2 * tempo)
sp.play_sounds([B,D], 2 * tempo)
sp.play_sounds([E], 1 * tempo)
sp.play_sounds([D], 1 * tempo)
sp.play_sounds([C,A], 2 * tempo)
sp.play_sounds([B,Gm], 2 * tempo)
sp.play_sounds([A,Em], 4 * tempo)
sp.play_sounds([A,Em], 2 * tempo)
sp.play_sounds([A,C], 2 * tempo)
sp.play_sounds([E,C], 4 * tempo)
sp.play_sounds([B,D], 2 * tempo)
sp.play_sounds([C,A], 2 * tempo)
sp.play_sounds([B,Gm], 2 * tempo)
sp.play_sounds([B,Em], 2 * tempo)
sp.play_sounds([B,Gm], 2 * tempo)
sp.play_sounds([C,A], 2 * tempo)
sp.play_sounds([B,D], 4 * tempo)
sp.play_sounds([C,E], 4 * tempo)
sp.play_sounds([C,A], 4 * tempo)
sp.play_sounds([A,Em], 4 * tempo)
sp.play_sounds([A,Em], 4 * tempo)
sp.play_sounds([A,Em], 4 * tempo)

"""
sp.play_sounds([F,A], 2 * tempo)
sp.play_sounds([C,AM], 4 * tempo)
sp.play_sounds([G,B], 2 * tempo)
sp.play_sounds([F,A], 2 * tempo)
sp.play_sounds([E,Gm], 1 * tempo)
sp.play_sounds([G,A], 1 * tempo)
"""

"""
sp.play_sounds([G], 0.5)
sp.play_sounds([G], 0.5)



sp.play_sounds([D], 0.5)
sp.play_sounds([E], 0.5)
sp.play_sounds([F], 0.5)
sp.play_sounds([D], 0.5)
sp.play_sounds([E], 0.5)
sp.play_sounds([G,A], 0.5)
sp.play_sounds([G], 0.5)
sp.play_sounds([G], 0.5)

sp.play_sounds([C], 0.5)
sp.play_sounds([B], 0.5)
sp.play_sounds([Bb], 0.5)
sp.play_sounds([Bb], 0.5)
sp.play_sounds([Bb,A], 0.5)
sp.play_sounds([G], 0.5)
sp.play_sounds([D], 0.5)

sp.play_sounds([C], 0.5)
sp.play_sounds([Bb], 0.5)
sp.play_sounds([A,A,G], 0.5)
sp.play_sounds([Gb], 0.5)
sp.play_sounds([G], 0.5)

sp.play_sounds([D], 0.5)
sp.play_sounds([E], 0.5)
sp.play_sounds([F], 0.5)
sp.play_sounds([E], 0.5)
sp.play_sounds([F], 0.5)

sp.play_sounds([Em], 0.5)
sp.play_sounds([C], 0.5)
sp.play_sounds([Em], 0.5)
sp.play_sounds([C], 0.5)

sp.play_sounds([Em], 0.5)
sp.play_sounds([C], 0.5)
sp.play_sounds([Em], 0.5)
sp.play_sounds([C], 0.5)
"""
# sp.play_song([(sound_a, 0.6),(sound_b, 0.4),(sound_c, 0.9),(sound_a, 0.5),(sound_b, 0.4)])

sp.close()
