#!/usr/bin/python3
import soundPlayer as pysounds

sp = pysounds.SoundPlayer(4)
A = pysounds.SoundFactory.get_sine_sound(440, 0.1)
B = pysounds.SoundFactory.get_square_sound(493.88, 0.1, 0.15)
C = pysounds.SoundFactory.get_square_sound(523.25, 0.1, 0.5)
D = pysounds.SoundFactory.get_square_sound(587.33, 0.1, 0.80)
E = pysounds.SoundFactory.get_square_sound(659.25, 0.1, 0.15)
F = pysounds.SoundFactory.get_square_sound(698.46, 0.1, 0.5)
G = pysounds.SoundFactory.get_square_sound(783.99, 0.1, 0.15)
Ab = pysounds.SoundFactory.get_square_sound(830.61, 0.1, 0.15)
AM = pysounds.SoundFactory.get_square_sound(880.00, 0.1, 0.8)
Gm = pysounds.SoundFactory.get_square_sound(392.00, 0.1, 0.8)
Em = pysounds.SoundFactory.get_square_sound(329.63, 0.1, 0.8)

Drum = pysounds.SoundFactory.get_noise_sound(150, 0.1)
sp.play_sounds([Drum], 0.1)
sp.play_sounds([E, B], 4 * 0.1)
sp.play_sounds([Drum], 0.1)
sp.play_sounds([E, B], 4 * 0.1)
sp.play_sounds([Drum], 0.1)

tempo = 0.05
sp.play_sounds([E, B], 4 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([Drum, A, C], 2 * tempo)
sp.play_sounds([Drum, D, B, D], 2 * tempo)
sp.play_sounds([E], 1 * tempo)
sp.play_sounds([D], 1 * tempo)
sp.play_sounds([A, C, Drum], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([E, C], 4 * tempo)
sp.play_sounds([B, D], 2 * tempo)
sp.play_sounds([C, A], 2 * tempo)
sp.play_sounds([B, Gm, Drum], 2 * tempo)
sp.play_sounds([B, Em, Drum], 2 * tempo)
sp.play_sounds([B, Gm, Drum], 2 * tempo)
sp.play_sounds([C, A], 2 * tempo)
sp.play_sounds([B, D], 4 * tempo)
sp.play_sounds([C, E], 4 * tempo)
sp.play_sounds([C, A], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)

# sp.play_song([(sound_a, 0.6),(sound_b, 0.4),(sound_c, 0.9),(sound_a, 0.5),(sound_b, 0.4)])

sp.close()
