# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 18:27:19 2023

@author: jjjimenez
"""

def señalBeep():
    import winsound
    import time
    
    # Define la frecuencia y duración de los pitidos
    short_beep_freq = 2000 # Hz
    long_beep_freq = 3000 # Hz
    beep_duration = 150 # milisegundos
    
    # Genera la secuencia de pitidos
    winsound.Beep(short_beep_freq, beep_duration) # Pitido corto
    time.sleep(0.1) # Espera 0.1 segundos entre pitidos
    winsound.Beep(short_beep_freq, beep_duration) # Pitido corto
    time.sleep(0.1) # Espera 0.1 segundos entre pitidos
    winsound.Beep(short_beep_freq, beep_duration) # Pitido corto
    time.sleep(0.2) # Espera 0.2 segundos entre pitidos
    winsound.Beep(long_beep_freq, beep_duration*4) # Pitido largo


señalBeep()     