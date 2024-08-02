import arcade
from arcade.experimental.uislider import UISlider
from arcade.gui import UIManager, UIAnchorWidget, UILabel

class UIMockup(arcade.Window):
    def __init__(self):

        super().__init__(800, 600, "Тесты", resizable=True)
        self.manager = UIManager()
        self.manager.enable()
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        ui_slider = UISlider(value=0, width=600, height=30)
        self.manager.add(UIAnchorWidget(child=ui_slider, anchor_y='bottom', align_y= 150))

        play_button = arcade.gui.UIFlatButton(text="||",size_hint=0.5)
        self.manager.add(arcade.gui.UIAnchorWidget(child=play_button, anchor_y='bottom',align_y = 50))
        self.check = True

        next_button = arcade.gui.UIFlatButton(text=">", width=30, height= 30)
        self.manager.add(arcade.gui.UIAnchorWidget(child=next_button, anchor_y='bottom',align_y= 60, align_x=70))

        pre_button = arcade.gui.UIFlatButton(text="<", width=30, height=30, )
        self.manager.add(arcade.gui.UIAnchorWidget(child=pre_button, anchor_y='bottom', align_y=60, align_x=-70))

        play_button.on_click = self.on_click_pause
        next_button.on_click = self.on_click_next
        pre_button.on_click = self.on_click_pre


    def on_click_pause(self,event):
        if self.check:
            print("Поставили на паузу")
            self.check = False
        else:
            print("Сняли с паузы пук")
            self.check = True

    def on_click_next(self,event):
        print("След трек")

    def on_click_pre(self,event):
        print("Пред трек")


    def on_draw(self):
        self.clear()
        self.manager.draw()


if __name__ == '__main__':
    window = UIMockup()
    arcade.run()