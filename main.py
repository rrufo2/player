import pyglet
import sys
import os

class Play_List():
    def __init__(self,name):
        self.name = name
        if os.path.exists(f"Playlists/{self.name}"):
            pass
        else:
            self.file = open(f"playlists/{self.name}.txt", "a")
            self.file.close()

    def give_playlist(self):
        self.file = open(f"playlists/{self.name}.txt", "r")
        print(self.file.read())
        self.file.close()

    def name_to_list(self):
        self.lists = []
        with open(f"playlists/{self.name}.txt", "r") as self.file:
            self.lists = [self.lists.rstrip() for self.lists in self.file]
        return self.lists

    def add_track(self, track):
        self.file = open(f"playlists/{self.name}.txt", "a")
        for i in track:
            self.file.write(f"{i}\n")
        self.file.close()

    def rem_track(self, track):
        self.file = open(f"playlists/{self.name}.txt", "a")

    def create_playlist(self):
        pass

class Track():
    def __init__(self, track):
        self.path = f"music/{track}"
        self.player = pyglet.media.Player()
        self.source = pyglet.media.load(self.path)
        self.player.queue(self.source)

    def play_new_track(self, track):
        self.player.pause()
        self.source = pyglet.media.load(f"music/{track}")
        self.player.delete()
        self.player.queue(self.source)
        self.player.play()

    def play(self):
        if self.player.playing:
            self.player.pause()
        else:
            self.player.play()

    def return_status(self):
        return self.player.playing

    def return_length(self):
        return self.source.duration

    def pause(self):
        self.player.pause()

    def set_time(self, value):
        self.player.seek(value)

    def return_time(self):
        return self.player.time

    def set_volume(self, value_volume):
        self.player.volume = value_volume/100

    def next_track(self, track):
        self.source = pyglet.media.load(f"music/{track}")
        self.player.queue(self.source)