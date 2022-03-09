'''
Sign your name: Gabe Van Haecke
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Box class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!

'''
import arcade


SW = 500
SH = 500


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.laser = arcade.load_sound("sounds/laser.mp3")
        self.explosion = arcade.load_sound("sounds/explosion.mp3")

    def draw(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)

    def update(self):
        if not -self. rad/2 + self.pos_y + self.dy < 0 and not self. rad/2 + self.pos_y + self.dy > SH:
            self.pos_y += self.dy
        else:
            arcade.play_sound(self.explosion)
        if not -self. rad/2 + self.pos_x + self.dx < 0 and not self. rad/2 + self.pos_x + self.dx > SW:
            self.pos_x += self.dx
        else:
            arcade.play_sound(self.laser)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball = Box(120, 120, 0, 0, 50, arcade.color.AUBURN)
        self.ball2 = Box(120, 120, 0, 0, 50, arcade.color.BRIGHT_NAVY_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()

    def on_update(self, dt):
        self.ball.update()
        self.ball2.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.ball.dx = -3
        elif key == arcade.key.D:
            self.ball.dx = 3
        elif key == arcade.key.W:
            self.ball.dy = 3
        elif key == arcade.key.S:
            self.ball.dy = -3
        if key == arcade.key.LEFT:
            self.ball2.dx = -4
        elif key == arcade.key.RIGHT:
            self.ball2.dx = 4
        elif key == arcade.key.UP:
            self.ball2.dy = 4
        elif key == arcade.key.DOWN:
            self.ball2.dy = -4

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.dy = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball2.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball2.dy = 0


def main():
    window = MyGame(SW, SH, "13.0 Jedi Training")
    arcade.run()


if __name__ == "__main__":
    main()
