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
        ("\nYou said no interest", 0.10),
        ("You said he's swagged out", 0.05),
        ("You leave", 0.06),
        ("It's like a shot to the back", 0.07),
        ("Through the nose of a barrel", 0.07),
        ("You dont want to go", 0.08),
    ]
    delays = [0.3, 1.5, 5.3, 6.9 , 8.0, 10.0, 12,9]

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
