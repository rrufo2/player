import customtkinter as Tk



class App(Tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Плеер музыки")
        self.geometry("600x500")
        self.minsize(400,400)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=7)

        self.rowconfigure(0, weight=7)
        self.rowconfigure(1, weight=1)

        self.left_panel = Tk.CTkFrame(master=self, fg_color="green")
        self.left_panel.grid(row=0, column=0, sticky="nsew", )

        self.playlist_panel = Tk.CTkFrame(master=self, fg_color="grey")
        self.playlist_panel.grid(row=1, column=0, sticky="nsew")

        self.center_panel = Tk.CTkFrame(master=self, fg_color="blue")
        self.center_panel.grid(row=0, column=1, sticky="nsew")

        self.bottom_panel = Tk.CTkFrame(master=self, fg_color="grey")
        self.bottom_panel.grid(row=1,column=1,sticky="nsew")
        self.bottom_panel.grid_columnconfigure((0,1,2,3,4,5), weight=1)

        self.left_panel = Tk.CTkScrollableFrame(master=self.left_panel, fg_color="green", width=150)
        self.left_panel.grid(sticky="nsew")

        self.setting_button = Tk.CTkButton(master=self.bottom_panel, command=self.setting, text="Settings",
                                   corner_radius=10, width=10)
        self.setting_button.grid(row=1, column=0)

        self.pre_button = Tk.CTkButton(master=self.bottom_panel, command=self.pre_track, text="Pre",
                                   corner_radius=10, width=10)
        self.pre_button.grid(row=1, column=1)

        self.play_button = Tk.CTkButton(master=self.bottom_panel, command=self.play_pause, text="Play",
                                   corner_radius=10, width=10)
        self.play_button.grid(row=1, column=2, sticky="ew")

        self.next_button = Tk.CTkButton(master=self.bottom_panel, command=self.next_track, text="Next",
                                   corner_radius=10, width=10)
        self.next_button.grid(row=1, column=3)

        self.sound_button = Tk.CTkButton(master=self.bottom_panel, command=self.sound_value, text="Sound",
                                   corner_radius=10, width=10)
        self.sound_button.grid(row=1, column=4)

        self.sound_slider = Tk.CTkSlider(master=self.bottom_panel)
        self.sound_slider.grid(row=1, column=5)

        self.value_slider = Tk.CTkSlider(master=self.bottom_panel, progress_color="green")
        self.value_slider.grid(row=0, columnspan=6, padx=(10,10), pady=(10,10), sticky="ew")

    def play_pause(self):
        print("Play pressed")

    def pre_track(self):
        print("Пред трек")

    def next_track(self):
        print("След трек")

    def sound_value(self):
        print(f"Текущая громкость {int(round(self.value_slider._value,2)*100)}")

    def setting(self):
        print("Настройтки")




    def call_menu(self):
        pass






if __name__ == "__main__":
    app = App()
    app.mainloop()