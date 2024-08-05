import arcade
import os
from time import sleep
from arcade.experimental.uislider import UISlider
from arcade.gui import UIManager, UIAnchorWidget, UILabel
from main import Track_now
from main import Play_List
track2 = Track_now("music/", "Aberraciya_-_Prodolzhaem_bojj_(musmore.org).mp3", ".mp3")

defualt = Play_List(os.path.dirname(__file__) + "\\music\\")
class UIMockup(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Тесты", resizable=True)
        self.manager = UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        ui_slider_track = UISlider(value=track2.return_time(), width=600, height=30, max_value=100)
        self.manager.add(UIAnchorWidget(child=ui_slider_track, anchor_y='bottom', align_y= 150))
        self.manager.on_update(1)

        ui_slider_volume = UISlider(value=100, width=100, height=30)
        self.manager.add(UIAnchorWidget(child=ui_slider_volume, anchor_y='bottom', align_y=60, anchor_x="center", align_x=200))

        self.texture_hovered_play = arcade.load_texture(":resources:onscreen_controls/shaded_dark/play.png")
        self.texture_play = arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png")
        self.texture_hovered_pause = arcade.load_texture(":resources:onscreen_controls/shaded_dark/pause_square.png")
        self.texture_pause = arcade.load_texture(":resources:onscreen_controls/flat_dark/pause_square.png")

        self.play_button = arcade.gui.UITextureButton(texture=self.texture_play,
                                                      texture_hovered=self.texture_hovered_play)
        self.play_button.on_update(0.1)
        self.manager.add(arcade.gui.UIAnchorWidget(child=self.play_button, anchor_y='bottom', align_y=20, align_x=-200))


        next_button = arcade.gui.UIFlatButton(text=">", width=30, height= 30)
        self.manager.add(arcade.gui.UIAnchorWidget(child=next_button, anchor_y='bottom', align_y=30, align_x=-150))

        pre_button = arcade.gui.UIFlatButton(text="<", width=30, height=30, )
        self.manager.add(arcade.gui.UIAnchorWidget(child=pre_button, anchor_y='bottom', align_y=30, align_x=-250))

        @ui_slider_volume.event()
        def on_change(event):
            track2.set_volume(ui_slider_volume.value)

        @ui_slider_track.event()
        def on_change(event):
            length_track = track2.return_length()
            correct_time = (ui_slider_track.value * length_track)/100
            track2.set_time(correct_time)
            print(correct_time)

        @self.play_button.event("on_click")
        def pause(event):
            if track2.return_status():
                track2.pause()
                self.play_button = arcade.gui.UITextureButton(texture=self.texture_pause,
                                                              texture_hovered=self.texture_hovered_pause)
            else:
                track2.play()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.texture_hovered_play = arcade.load_texture(":resources:onscreen_controls/shaded_dark/pause_square.png")
        self.texture_play = arcade.load_texture(":resources:onscreen_controls/flat_dark/pause_square.png")

    def update(self, delta_time: float):
        pass

    def on_draw(self):
        self.clear()
        self.manager.draw()

if __name__ == '__main__':
    window = UIMockup()
    window.update(1)
    arcade.run()