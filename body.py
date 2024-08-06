import customtkinter as Tk
import os
from PIL import Image



class App(Tk.CTk):
    def __init__(self):
        super().__init__()
        self.music_files = os.listdir("music/")

        self._fg_color = "#2a1c36"
        self._set_appearance_mode("dark")
        self.title("Плеер музыки")
        self.geometry("600x400")
        self.minsize(600, 400)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=0)

        self.tc = "#d567db"
        self.bc = "#402952"#"#141c21"
        self.bgc = "#6a458a"

        self.play_image = Tk.CTkImage(dark_image=Image.open("images/play.png"), size=(20, 20))


        #Фрейм плейлиста
        self.LT_panel = Tk.CTkScrollableFrame(master=self, fg_color=self.bgc)
        self.LT_panel.grid(row=0, column=0, sticky="nsew", padx=(10,10), pady=(10,10))
        self.LT_panel.grid_columnconfigure(0, weight=1)
        self.LT_panel.grid_rowconfigure(0, weight=1)

        #Фрейм выбора плейлиста
        self.LB_panel = Tk.CTkFrame(master=self, fg_color="transparent")
        self.LB_panel.grid(row=1, column=0, sticky="nsew", padx=(10,10), pady=(10,10))
        self.LB_panel.grid_columnconfigure(0, weight=1)
        self.LB_panel.grid_rowconfigure(0, weight=1)

        #Фрейм центрального окна
        self.center_panel = Tk.CTkFrame(master=self, fg_color="#6a458a")
        self.center_panel.grid(row=0, column=1, sticky="nsew", padx=(10,10), pady=(10,10))
        self.center_panel.grid_columnconfigure((0,1), weight=1)
        self.center_panel.grid_rowconfigure((0,1),weight=1)

        #Фрейм нижней панели
        self.bottom_panel = Tk.CTkFrame(master=self, corner_radius=10,
                                        fg_color=self.bgc)
        self.bottom_panel.grid(row=1,column=1,sticky="nsew", padx=(10, 10), pady=(10, 10))
        self.bottom_panel.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        #Выбор плейлиста(Левый низ)
        self.list_playlists = Tk.CTkComboBox(master=self.LB_panel, values=["Трек1","Трек2","Трек3","Трек4"],
                                             command=self.get_track,
                                             fg_color=self.bgc, text_color=self.tc, border_color=self.bgc,
                                             button_color="#1a252b", dropdown_fg_color=self.bgc,
                                             dropdown_text_color=self.tc)
        self.list_playlists.grid(row=0, column=0,sticky="new")


        #Текщуий плейлист(Левый верх)
        self.i = 0
        for self.i in range(len(self.music_files)):
            Tk.CTkFrame(master=self.LT_panel, height=50,fg_color=self.bc).grid(row=self.i,pady=(2, 2), padx=(2, 2), sticky="ew")
            Tk.CTkButton(master=self.LT_panel, text="del", fg_color=self.bc, bg_color=self.bc,
                         corner_radius=10, width=30, text_color=self.tc).grid(row = self.i, sticky="e", padx=(10,10))
        Tk.CTkFrame(master=self.LT_panel, height=50,fg_color=self.bc).grid(pady=(2, 2), padx=(2, 2), sticky="ew")
        Tk.CTkButton(master=self.LT_panel, text="+", fg_color=self.bc, bg_color=self.bc,
                         corner_radius=10, width=30, text_color=self.tc).grid(row=self.i+1)



        #Централое окно
        self.value_slider = Tk.CTkSlider(master=self.center_panel, height=15)
        self.value_slider.set(0)
        self.value_slider.grid(columnspan=2,row=1,padx=(10, 10), pady=(10,10), sticky="swe")


        # Нижнее меню(плей, громкость, след\пред трек, инфа)
        self.setting_button = Tk.CTkButton(master=self.bottom_panel, command=self.setting, text="Settings",
                                   corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.setting_button.grid(row=0, column=0, padx=(5, 5))

        self.pre_button = Tk.CTkButton(master=self.bottom_panel, command=self.pre_track, text="Pre",
                                   corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.pre_button.grid(row=0, column=1, padx=(5, 5))

        self.play_button = Tk.CTkButton(master=self.bottom_panel, command=self.play_pause,text="", image=self.play_image,
                                   corner_radius=10, width=20, height=20,  text_color=self.tc, fg_color=self.bc)
        self.play_button.grid(row=0, column=2, sticky="nsew", padx=(5, 5))

        self.next_button = Tk.CTkButton(master=self.bottom_panel, command=self.next_track, text="Next",
                                   corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.next_button.grid(row=0, column=3, padx=(5, 5))

        self.sound_button = Tk.CTkButton(master=self.bottom_panel, command=self.sound_value, text="Sound",
                                   corner_radius=10, width=10, text_color=self.tc, fg_color=self.bc)
        self.sound_button.grid(row=0, column=4, padx=(5, 5))

        self.sound_slider = Tk.CTkSlider(master=self.bottom_panel, width=50, height=10)
        self.sound_slider.grid(row=0, column=5, padx=(5, 5))
        self.sound_slider.set(1)


    def play_pause(self):
        print("Play pressed")

    def pre_track(self):
        print("Пред трек")

    def next_track(self):
        print("След трек")

    def sound_value(self):
        print(f"Текущая громкость {int(round(self.sound_slider._value,2)*100)}")

    def setting(self):
        print("Настройтки")

    def get_track(self, choice):
        print(f"Сейчас играет {choice}")






    def call_menu(self):
        pass






if __name__ == "__main__":
    app = App()
    app.mainloop()