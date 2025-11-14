import time 
import sys 

def print_lyrics():
    lyrics = [
        "And I was running far away",
        "Would I run off the world someday?",
        "Nobody knows, nobody knows",
        "I was dancing in the rain",
        "I felt alive and I can't complain",
        "But now take me home",
        "Take me home where I belong",
        "I can't take it anymore"
    ]

    delays = [
        0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.8,
    ]

    print("AURORA Runaway: \n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)

print_lyrics()