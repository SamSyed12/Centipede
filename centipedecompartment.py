import arcade

class centipede_compartment:
    def __init__(self, x, y, size, color):
        self.center_x = x
        self.center_y = y
        self.color = color
        self.width1 = 1000
        self.height1 = 500
        self.size = size
        self.x_dir = -1
        self.speed = 7


    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.size ,self.size , self.color)
        self.center_x += self.speed * self.x_dir
        if self.center_x - self.size < 0 or self.center_x + self.size > 1000 and self.center_y > 50:
            self.x_dir *= -1
            self.center_y -= self.size + 1
        elif self.center_x - self.size < 0 or self.center_x + self.size > 1000:
            self.x_dir *= -1




