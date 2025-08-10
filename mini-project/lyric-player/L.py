import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nSungguh tak terasa", 0.09),
        ("Sudah tujuh tahun", 0.10),
        ("Rotasi waktu hidupku", 0.10),
        ("Binar mata yang membiru", 0.09),
        ("Hari hari yang lesu", 0.07),
        ("Aku menunggu kamu", 0.10),
        ("Selalu aku lihat belakang punggungmu", 0.09),
        ("Disaat kau lihat belakang punggung pria lain", 0.10),
        ("Menunggu kau menoleh dan berlari ke arahku", 0.10),
        ("dan memelukku seerat-eratny", 0.09),
    ]
    delays = [0.1, 0.5, 4.0, 7.9, 12.3]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
        sing_song()
