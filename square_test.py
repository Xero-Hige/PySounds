#!/usr/bin/python3
import soundPlayer as pysounds

duty_cycle = 0.10

sp = pysounds.SoundPlayer(2)
A = pysounds.SoundFactory.get_square_sound(440, 0.1, duty_cycle*8)
B = pysounds.SoundFactory.get_square_sound(493.88, 0.1)
C = pysounds.SoundFactory.get_square_sound(523.25, 0.1, duty_cycle)
D = pysounds.SoundFactory.get_square_sound(587.33, 0.1, duty_cycle*5)
E = pysounds.SoundFactory.get_square_sound(659.25, 0.1, duty_cycle*5)
G = pysounds.SoundFactory.get_square_sound(783.99, 0.1, duty_cycle*3)
Gm = pysounds.SoundFactory.get_square_sound(392.00, 0.1, duty_cycle*3.5)
Em = pysounds.SoundFactory.get_square_sound(329.63, 0.1, duty_cycle*7.5)

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

sp.close()
