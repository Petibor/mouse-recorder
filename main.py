import mouse;
import keyboard

events = []
recording = False
playing = False


def record():
    print('Mouse Record started. The program will record till right click')
    global events
    global recording
    events = mouse.record(button='right')
    recording = False


def play():
    global events;
    global playing;
    mouse.play(events, 0.7)
    playing = False


while True:
    try:

        if keyboard.is_pressed('ctrl+shift') and recording == False:
            print('Record Started')
            recording = True
            record()
            print('Record ended')

        if keyboard.is_pressed('ctrl+alt') and recording == False & playing == False:
            print('Play Started. Press right click after play')
            playing = True
            play()

            print('Play Ended')


    except:
        break
