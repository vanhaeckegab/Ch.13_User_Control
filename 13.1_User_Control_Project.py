'''
USER CONTROL PROJECT
-----------------
Your choice!!! Have fun and be creative.
Create a background and perhaps animate some objects.
Pick a user control method and navigate an object around your screen.
Make your object more interesting than a ball.
Create your object with a new class.
Perhaps move your object through a maze or move the object to avoid other moving objects.
Incorporate some sound.
Type the directions to this project below:

DIRECTIONS:
----------
Please type directions for this game here.

'''
import arcade
import random

SW = 500
SH = 500


class Pointer:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c

    def draw_point(self):
        arcade.draw_circle_outline(self.x, self.y, self.r * 1.2, arcade.color.BLACK, 10)
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)


class Game:
    def __init__(self, gx, gy, rx, ry, bx, by, yx, yy):
        self.gx = gx
        self.gy = gy
        self.gs = arcade.load_sound("sounds/green.mp3")
        self.rx = rx
        self.ry = ry
        self.rs = arcade.load_sound("sounds/red.mp3")
        self.bx = bx
        self.by = by
        self.bs = arcade.load_sound("sounds/blue.mp3")
        self.yx = yx
        self.yy = yy
        self.ys = arcade.load_sound("sounds/yellow.mp3")

    def draw_game(self):
        arcade.draw_rectangle_filled(self.gx, self.gy, SW/2, SH/2, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.rx, self.ry, SW/2, SH/2, arcade.color.RED)
        arcade.draw_rectangle_filled(self.bx, self.by, SW/2, SH/2, arcade.color.BLUE)
        arcade.draw_rectangle_filled(self.yx, self.yy, SW/2, SH/2, arcade.color.YELLOW)

    def green_hit(self):
        self.gx += SW
        arcade.Sound.play(self.gs)
        if arcade.Sound.is_complete(self.gs, arcade.play_sound(self.gs)):
            self.gx -= SW
            print("1")

    def red_hit(self):
        self.rx += SW
        arcade.play_sound(self.rs)
        self.rx -= SW

    def blue_hit(self):
        self.bx += SW
        arcade.play_sound(self.bs)
        self.bx -= SW

    def yellow_hit(self):
        self.yx += SW
        arcade.play_sound(self.ys)
        self.yx -= SW


class Start:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

    def draw_start(self):
        arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, arcade.color.WHITE, 3)
        arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.c)
        arcade.draw_text("Start", self.x, self.y, arcade.color.BLACK, self.h * 3/4, 0, "center", "Impact", False,
                         False, "center", "center")


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.point = Pointer(SW/2, SH/2, SW/50, arcade.color.WHITE)
        self.game = Game(SW/4 - SW, SH * 3/4, SW * 3/4 - SW, SH * 3/4, SW * 3/4 - SW, SH/4,
                         SW/4 - SW, SH/4)
        self.start = Start(SW/2, SH/2, SW/10, SH/20, arcade.color.GOLD)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, SW/2, SH, SH/2, arcade.color.DARK_GREEN)
        arcade.draw_lrtb_rectangle_filled(SW/2, SW, SH, SH/2, arcade.color.DARK_RED)
        arcade.draw_lrtb_rectangle_filled(SW/2, SW, SH/2, 0, arcade.color.DARK_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, SW/2, SH/2, 0, arcade.color.DARK_YELLOW)
        self.game.draw_game()
        arcade.draw_rectangle_filled(SW/2, SH/2, SW/50, SH, arcade.color.BLACK)
        arcade.draw_rectangle_filled(SW/2, SH/2, SW, SH/50, arcade.color.BLACK)
        arcade.draw_circle_filled(SW/2, SH/2, SW/12.5, arcade.color.BLACK)
        self.start.draw_start()
        self.point.draw_point()

    def on_mouse_motion(self, x, y, dx, dy):
        self.point.x = x
        self.point.y = y

    def on_mouse_press(self, x, y, button, mod):
        if self.point.x < SW/2 and self.point.y > SH/2:
            if self.game.gx < 0:
                self.game.green_hit()
            else:
                pass
        elif self.point.x > SW/2 and self.point.y > SH/2:
            if self.game.rx < 0:
                self.game.red_hit()
            else:
                pass
        elif self.point.x > SW/2 and self.point.y < SH/2:
            if self.game.bx < 0:
                self.game.blue_hit()
            else:
                pass
        elif self.point.x < SW/2 and self.point.y < SH/2:
            if self.game.yx < 0:
                self.game.yellow_hit()
            else:
                pass


def main():
    window = MyGame(SW, SH, "Simon")
    arcade.run()


if __name__ == '__main__':
    main()
