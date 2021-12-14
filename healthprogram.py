# Health Programmer
# 9 AM - 5PM
# Water - water.mp3 (3.5ltr) - pani pina h -log - every - 40min
# Eye - eye.mp3 - every 30min - eyedone-log - every - 40min
# Physical activity - physical.mp3 every - 45 min - exdone - log
# Rule
#Pygame module to play audio



from pygame import mixer  
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__== '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_execise = time()
    watersecs = 5
    exsece = 10
    eyessece = 20

    while True:
        if time() - init_water > watersecs:
            print("water drinking time. Enter 'drank' to stop than alarm.")
            musiconloop("water.mp3", 'drank')
            init_water = time()
            log_now("drank water at")

        if time() - init_eyes > eyessecs:
            print("Eye execise time. Enter 'doneeyes' to stop than alarm.")
            musiconloop("eyes.mp3", 'doneeyes')
            init_water = time()
            log_now("Eyes Relaxed at")

        if time() - init_execise > exsece:
            print("Physical activities time. Enter 'donephy' to stop than alarm.")
            musiconloop("exsece.mp3", 'donephy')
            init_water = time()
            log_now("Physical activites at")






