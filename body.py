import customtkinter as Tk
import os
from PIL import Image

from main import Play_List
from main import Track


class App(Tk.CTk):
    def __init__(self):
        super().__init__()
        self.queue_tracks = 0
        self.playlists_name = []
        self.default_playlist = Play_List("Стандартный")
        self.default_playlist.add_track(os.listdir("music/"))

        self.playlists_name.append(self.default_playlist.name)
        self.test = self.default_playlist.name_to_list()[self.queue_tracks]
        self.music = Track(self.test)

        self._fg_color = "#252a2b"
        self._set_appearance_mode("dark")
        self.title("Плеер музыки")
        self.geometry("700x500")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=0)

        self.tc = "#3e9cfa"
        self.bc = "#3b3c40"
        self.bgc = "#43494a"

        self.play_image = Tk.CTkImage(dark_image=Image.open("images/play.png"), size=(20, 20))

        # Фрейм плейлиста
        self.LT_panel = Tk.CTkScrollableFrame(master=self, fg_color=self.bgc)
        self.LT_panel.grid(row=0, column=0, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.LT_panel.grid_columnconfigure(0, weight=1)
        self.LT_panel.grid_rowconfigure(0, weight=1)

        # Фрейм выбора плейлиста
        self.LB_panel = Tk.CTkFrame(master=self, fg_color="transparent")
        self.LB_panel.grid(row=1, column=0, sticky="ew", padx=(10, 10), pady=(10, 10))
        self.LB_panel.grid_columnconfigure(0, weight=1)
        self.LB_panel.grid_rowconfigure(0, weight=1)

        # Фрейм центрального окна
        self.center_panel = Tk.CTkFrame(master=self, fg_color=self.bgc)
        self.center_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.center_panel.grid_columnconfigure((0, 1), weight=1)
        self.center_panel.grid_rowconfigure((0, 1), weight=1)

        # Фрейм нижней панели
        self.bottom_panel = Tk.CTkFrame(master=self, corner_radius=10,
                                        fg_color=self.bgc)
        self.bottom_panel.grid(row=1, column=1, sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.bottom_panel.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.bottom_panel.grid_rowconfigure(0, weight=1)

        # Выбор плейлиста(Левый низ)
        self.list_playlists = Tk.CTkComboBox(master=self.LB_panel, values=self.playlists_name,
                                             command=self.get_track,
                                             fg_color=self.bgc, text_color=self.tc, border_color=self.bgc,
                                             button_color="#1a252b", dropdown_fg_color=self.bgc,
                                             dropdown_text_color=self.tc)
        self.list_playlists.grid(row=0, column=0, sticky="new")

        self.add_entry = Tk.CTkEntry(master=self.LB_panel, placeholder_text="Введите название нового плейлиста", )
        self.add_entry.grid(row=1, column=0, sticky="ew", pady=(10, 10), padx=(0, 25))

        self.add_button = Tk.CTkButton(master=self.LB_panel, width=25, text="+")
        self.add_button.grid(row=1, column=0, sticky="e", pady=(10, 10))

        # Текщуий плейлист(Левый верх)
        self.i = 0
        self.list_frames = []
        for self.i in range(len(self.default_playlist.name_to_list())):
            a = Tk.CTkFrame(master=self.LT_panel, height=50, fg_color=self.bc).grid(row=self.i, pady=(2, 2),
                                                                                    padx=(2, 2), sticky="ew")
            Tk.CTkButton(master=self.LT_panel, text="del", fg_color=self.bc, bg_color=self.bc,
                         corner_radius=10, width=30, text_color=self.tc,
                         command=self.del_track).grid(row=self.i, sticky="e", padx=(10, 10))
            Tk.CTkLabel(master=self.LT_panel, text=self.default_playlist.name_to_list()[self.i], anchor="w",
                        justify="left",
                        bg_color=self.bc, text_color=self.tc).grid(row=self.i, sticky="ew", padx=(10, 60))

            self.list_frames.append(a)
        Tk.CTkFrame(master=self.LT_panel, height=50, fg_color=self.bc).grid(pady=(2, 2), padx=(2, 2), sticky="ew")
        Tk.CTkButton(master=self.LT_panel, text="+", fg_color=self.bc, bg_color="transparent",
                     corner_radius=10, width=30, text_color=self.tc, command=self.add_track).grid(row=self.i + 1,
                                                                                                  sticky="nsew")

        # Централое окно
        self.value_slider = Tk.CTkSlider(master=self.center_panel, height=15, command=self.set_value_track)
        self.value_slider.set(0)
        self.value_slider.grid(columnspan=3, row=2, padx=(10, 10), pady=(0, 10), sticky="swe")

        # self.progress_track = Tk.CTkProgressBar(master=self.center_panel, height=15, determinate_speed=1/self.music.return_length())
        # print(100/self.music.return_length())
        # self.progress_track.set(0)
        # self.progress_track.grid(columnspan=3, row=2, padx=(10, 10), pady=(0, 10), sticky="swe")

        self.this_second = Tk.CTkLabel(master=self.center_panel, text="0.00")
        self.this_second.grid(row=1, column=0, padx=(10, 10), sticky="sw")

        self.length_track = Tk.CTkLabel(master=self.center_panel,
                                        text=self.convert_to_normal_time(self.music.return_length()))
        self.length_track.grid(row=1, column=1, padx=(10, 10), sticky="se")

        # Нижнее меню(плей, громкость, след\пред трек, инфа)
        self.setting_button = Tk.CTkButton(master=self.bottom_panel, command=self.setting, text="Settings",
                                           corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.setting_button.grid(row=0, column=0, padx=(5, 5))

        self.pre_button = Tk.CTkButton(master=self.bottom_panel, command=self.pre_track, text="Pre",
                                       corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.pre_button.grid(row=0, column=1, padx=(5, 5))

        self.play_button = Tk.CTkButton(master=self.bottom_panel, command=self.play_pause, text="",
                                        image=self.play_image,
                                        corner_radius=10, text_color=self.tc, fg_color=self.bc, width=15, height=15)
        self.play_button.grid(row=0, column=2, padx=(5, 5))

        self.next_button = Tk.CTkButton(master=self.bottom_panel, command=self.next_track, text="Next",
                                        corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.next_button.grid(row=0, column=3, padx=(5, 5))

        self.sound_button = Tk.CTkButton(master=self.bottom_panel, text="Sound",
                                         corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.sound_button.grid(row=0, column=4, padx=(5, 5))

        self.sound_slider = Tk.CTkSlider(master=self.bottom_panel, width=50, height=10, command=self.sound_value)
        self.sound_slider.grid(row=0, column=5, padx=(5, 5))
        self.sound_slider.set(1)

    def play_pause(self):
        self.music.play_pause()

    def pre_track(self):
        if self.queue_tracks == 0:
            self.queue_tracks = len(self.default_playlist.name_to_list()) - 1
        else:
            self.queue_tracks -= 1
        self.source = self.default_playlist.name_to_list()[self.queue_tracks]
        self.music.play_new_track(self.source)

        self.length_track.configure(text=self.convert_to_normal_time(self.music.return_length()))
        self.this_second.configure(text="0.00")
        self.value_slider.set(0)
        print(f"Сейчас играеи - {self.default_playlist.name_to_list()[self.queue_tracks]}")

    def next_track(self):
        if self.queue_tracks == len(self.default_playlist.name_to_list()) - 1:
            self.queue_tracks = 0
        else:
            self.queue_tracks += 1
        self.source = self.default_playlist.name_to_list()[self.queue_tracks]
        self.music.play_new_track(self.source)
        self.length_track.configure(text=self.convert_to_normal_time(self.music.return_length()))
        self.this_second.configure(text="0.00")
        self.value_slider.set(0)
        print(f"Сейчас играеи - {self.default_playlist.name_to_list()[self.queue_tracks]}")

    def sound_value(self, value):
        self.music.set_volume(round(value, 2))

    def setting(self):
        print("Настройтки")

    def get_track(self, choice):
        print(f"Сейчас играет {choice}")

    def set_value_track(self, value):
        self.len_track = self.music.return_length()  # round(value)
        self.this_second.configure(
            text=self.convert_to_normal_time(value * self.music.return_length()))
        print(round(round(value, 2) * self.music.return_length()))
        self.music.set_time(round(round(value, 2) * self.music.return_length()))
        self.music.player.play()

    def add_track(self):
        self.i += 1
        Tk.CTkFrame(master=self.LT_panel, height=50, fg_color=self.bc).grid(row=self.i, pady=(2, 2), padx=(2, 2),
                                                                            sticky="ew")
        Tk.CTkButton(master=self.LT_panel, text="del", fg_color=self.bc, bg_color=self.bc,
                     corner_radius=10, width=30, text_color=self.tc).grid(row=self.i, sticky="e", padx=(10, 10))
        Tk.CTkLabel(master=self.LT_panel, text="Новий трээээк", anchor="w", justify="left",
                    bg_color=self.bc, text_color=self.tc).grid(row=self.i, sticky="w", padx=(10, 60))

        self.default_playlist.add_track(["Новый трэээк"])

        Tk.CTkFrame(master=self.LT_panel, height=50, fg_color=self.bc).grid(pady=(2, 2), padx=(2, 2), sticky="ew")
        Tk.CTkButton(master=self.LT_panel, text="+", fg_color=self.bc, bg_color="transparent",
                     corner_radius=10, width=30, text_color=self.tc,
                     command=self.add_track).grid(row=self.i + 1, sticky="nsew")

    def del_track(self):
        pass

    def call_menu(self):
        pass

    def convert_to_normal_time(self, value):
        if 0 <= round(value) % 60 < 10:
            return f"{round(value) // 60}.0{round(value) % 60}"
        else:
            return f"{round(value) // 60}.{round(value) % 60}"


if __name__ == "__main__":
    app = App()
    app.mainloop()
