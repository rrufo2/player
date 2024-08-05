import customtkinter as Tk



class App(Tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Плеер музыки")
        self.geometry("600x500")
        self.minsize(400,400)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=10)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=2)


        self.left_panel = Tk.CTkScrollableFrame(master=self, fg_color="green")
        self.left_panel.grid(row=0, column=0,sticky="nsew")

        self.center_panel = Tk.CTkFrame(master=self, fg_color="blue")
        self.center_panel.grid(row=0, column=1, sticky="nsew")

        self.bottom_panel = Tk.CTkFrame(master=self, fg_color="transparent")
        self.bottom_panel.grid(row=1, column=1,sticky="nsew")

        self.button = Tk.CTkButton(master=self.bottom_panel, command=self.button_callback, text="Play",
                                   corner_radius=10, width=10)
        self.button.grid(row=1, column=1, sticky="nsew")

    def get_y_size(self):
        self.size_win = self.geometry()
        x = ""
        for i in range(len(self.size_win)):
            if self.size_win[i] == "x":
                return int(x)
            x += self.size_win[i]

    def get_x_size(self):
        self.size_win = self.geometry()
        y = ""
        for i in range(len(self.size_win)):
            if self.size_win[i] == "x":
                for j in range(i + 1, len(self.size_win), 1):
                    if self.size_win[j] == "+":
                        return int(y)
                    y += self.size_win[j]

    def button_callback(self):
        print("button pressed")
        print(self.get_x_size())
        print(self.get_y_size())
        print(self.winfo_width())

    def call_menu(self):
        pass






if __name__ == "__main__":
    app = App()
    app.mainloop()