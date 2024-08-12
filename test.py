import pyglet
from time import sleep

player = pyglet.media.Player()


source = pyglet.media.load("music/Aberraciya_-_Prodolzhaem_bojj_(musmore.org).mp3")
player.queue(source=source)
player.play()
player.volume = 0.01

while True:
    a = input()
    if a == "1":
        break
    player.seek_next_frame()

    if player.playing:
        print("Aboba")

    player.play()