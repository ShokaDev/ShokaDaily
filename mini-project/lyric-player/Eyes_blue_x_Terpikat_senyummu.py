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
        ("\nPergilah-pergi", 0.08),
        ("Kau takkan peduli", 0.06),
        ("Kan ku coba lagi", 0.07),
        ("Tuk belajar mencintai", 0.08),
        (" ", 0.01),
        ("Eyes blue or brown can't remember", 0.05),
        (" ", 0.01),
        ("Tak lagi terpikat", 0.06)
        ("Senyum mu yang mabukanku", 0.07),
        (" ", 0.01), 
        ("Eyes green or grey, can't remember", 0.05),
        (" ", 0.5),
        ("Harusnya 'ku tau", 0.07),
        ("Memang kau bukan milikku", 0.07),
        (" ", 0.01),
    ]
    delays = [1.0, 2.0, 2.7, 3.2, 4.1, 7.9, 8.0, 9.0, 10.0, 12.0, 12.1, 15.0, 15.1, 16.0, 17.0]

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
