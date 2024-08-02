import arcade
import sys
import os
class Music():
    def __init__(self, path, name, format):
        self.path = path
        self.name = name
        self.format = format
        self.sound = arcade.load_sound(self.path + self.name)

class Play(Music):
    def __init__(self, path, name, format):
        Music.__init__(self, path, name, format)
        self.check = True
    def play(self):
       self.playing  = arcade.play_sound(self.sound, 0.2, 0, False, 1)
    def pause(self):
        if self.check == True:
            arcade.stop_sound(self.playing)
            self.check = False
