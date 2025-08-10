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
        ("\nI'll imagine we fell in love", 0.08),
        ("I'll nap under moonlight skies with you", 0.09),
        ("I think I'll picture us, you with the waves", 0.09),
        ("The ocean's colors on your face", 0.08),
        ("I'll leave my heart with your air", 0.16),
        ("So let me fly with you", 0.11),
        ("Will you be forever with me?", 0.19),
        (" ", 0.01),
    ]
    delays = [1.0, 2.0, 2.7, 3.2, 6.1, 9.2, 10.0, 10.1]

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