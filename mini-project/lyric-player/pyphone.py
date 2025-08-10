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
        ("\nBahasa inggrisnya jika, apa ya?", 0.09),
        (" ", 0.10),
        ("If 'Happy Ever After' did exist", 0.10),
        ("I would still be holding you like this", 0.09),
        ("All those fairytales are full of shit", 0.07),
        ("One more fucking love song, I'll be sick", 0.09)
    ]
    delays = [0.1, 0.5, 4.0, 7.9, 12.3, 15.6]

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
