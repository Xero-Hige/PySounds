#!/usr/bin/python3
import soundPlayer as pysounds

dc = 0.80

sp = pysounds.SoundPlayer(2)
A = pysounds.SoundFactory.get_square_sound(440, 0.1, dc)
B = pysounds.SoundFactory.get_square_sound(493.88, 0.1, dc)
C = pysounds.SoundFactory.get_square_sound(523.25, 0.1, dc)
D = pysounds.SoundFactory.get_square_sound(587.33, 0.1, dc)
E = pysounds.SoundFactory.get_square_sound(659.25, 0.1, dc)
F = pysounds.SoundFactory.get_square_sound(698.46, 0.1, dc)
G = pysounds.SoundFactory.get_square_sound(783.99, 0.1, dc)
Ab = pysounds.SoundFactory.get_square_sound(830.61, 0.1, dc)
AM = pysounds.SoundFactory.get_square_sound(880.00, 0.1, dc)
Gm = pysounds.SoundFactory.get_square_sound(392.00, 0.1, dc)
Em = pysounds.SoundFactory.get_square_sound(329.63, 0.1, dc)

tempo = 0.1
sp.play_sounds([E, B], 4 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([B, D], 2 * tempo)
sp.play_sounds([E], 1 * tempo)
sp.play_sounds([D], 1 * tempo)
sp.play_sounds([C, A], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([E, C], 4 * tempo)
sp.play_sounds([B, D], 2 * tempo)
sp.play_sounds([C, A], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([B, Em], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([C, A], 2 * tempo)
sp.play_sounds([B, D], 4 * tempo)
sp.play_sounds([C, E], 4 * tempo)
sp.play_sounds([C, A], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)

# sp.play_song([(sound_a, 0.6),(sound_b, 0.4),(sound_c, 0.9),(sound_a, 0.5),(sound_b, 0.4)])

sp.close()
