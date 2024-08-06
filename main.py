import pyglet
import sys
import os

class Play_List():
    def __init__(self,path):
        self.tracks = os.listdir(path)
    def give_playlist(self):
        print(self.tracks)

class Music():
    def __init__(self, path:str, name:str, format:str):
        self.path = path
        self.name = name
        self.format = format
        self.player = pyglet.media.Player()
        self.sourse = pyglet.media.load(self.path + self.name)
        self.player.queue(self.sourse)

class Track_now(Music):

    def play(self):
        self.player.play()

    def return_status(self):
        return self.player.playing

    def return_length(self):
        return self.sourse.duration

    def pause(self):
        self.player.pause()

    def set_time(self, value):
        self.player.seek(value)

    def return_name(self):
        return self.name

    def return_time(self):
        return self.player.time

    def set_volume(self, value_volume):
        self.player.volume = value_volume/100
