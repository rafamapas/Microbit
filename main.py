def on_gesture_shake():
    music.play(music.string_playable("E B C5 A B G A F ", 237),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(1000)
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
