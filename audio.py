import os
import time

def play_morse(morse):
    if os.path.exists("audio.png"):
        print("audio.png found")
    else:
        print("audio.png not found")

    try:
        import winsound
        for c in morse:
            if c==".":
                winsound.Beep(800,100)
            elif c=="-":
                winsound.Beep(800,300)
            elif c==" ":
                time.sleep(0.1)
            elif c=="/":
                time.sleep(0.4)
    except Exception as e:
        print("Audio unavailable:",e)