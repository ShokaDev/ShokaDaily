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
        ("\nLantas mengapa ku masih meanaruh hati", 0.10),
        (" ", 0.01),
        ("Lantas mengapa ku masih meanaruh hati", 0.10),
        ("Padahal kutahu kau t'lah terikat janji", 0.11),
        ("Keliru ataukah bukan tak tahu", 0.14),
        ("Lupakanmu tapi aku tak mau", 0.14),
        (" ", 0.01),
    ]
    delays = [0.3, 1.5, 5.0, 10.0, 14.0, 19.0, 23.0]

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
