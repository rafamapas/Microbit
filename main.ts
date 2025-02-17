input.onGesture(Gesture.Shake, function () {
    music.play(music.stringPlayable("E B C5 A B G A F ", 237), music.PlaybackMode.UntilDone)
    basic.pause(1000)
    basic.showNumber(randint(1, 6))
})
