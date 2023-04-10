import arcade


class firing_position:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y
        self.width = 50
        self.color = arcade.color.AIR_FORCE_BLUE
        self.speed = 1
        self.x_dir = 0
        self.y_dir = 0
        self.width1 = 1000
        self.height1 = 500


    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y , self.width, self.width, arcade.color.RED )

        self.center_x += self.speed * self.x_dir
        self.center_y += self.speed * self.y_dir

        if self.width1 - 50 < self.center_x or self.center_x + 50 < 0:
            self.x_dir *= -1
        elif self.height1 +50 < self.center_y or self.center_y - 50 < 0:
            self.center_y *= -1

    def turnleft(self):
        self.center_x -= 4

    def turnright(self):
        self.center_x += 4

    def returntocentre(self):
        if self.center_x -25  < 0 or self.center_x + 25 > 1000:
            self.center_x = 500







