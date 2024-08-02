import arcade
import sys
import os
class Play_List():
    def __init__(self, number):
        self.number = number
        self.path = os.listdir(r"C:\Users\James Cock\PycharmProjects\player\music")
        self.track_now = self.path[self.number]
        print(self.path)
    def next_play(self):
        self.number = self.number + 1
    def back_play(self):
        if self.number > 0:
            self.number = self.number - 1

class Music():
    def __init__(self, path, name, format):
        Play_List.__init__(self)
        self.path = path
        self.name = name
        self.format = format
        self.sound = arcade.Sound('music/' + self.track_now, True)


class Play(Music):
    def __init__(self, path, name, format):
        Music.__init__(self, path, name, format)
        self.check = bool
        self.position = float
        self.playing = None
    def play(self):
        if self.playing == None:
            self.playing  = arcade.play_sound(self.sound, 1, 0, False, 150)
            self.check = True
        if arcade.Sound.is_playing(self, self.playing) == False:
            self.check = False
            self.playing = None


    def pause(self):
        if self.check == True:
            arcade.Sound.stop(self, self.playing)
            self.position = arcade.Sound.get_stream_position(self, self.playing)
            self.check = False
            self.playing = None




