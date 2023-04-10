import arcade



class rocks:
    def __init__(self, x, y, width, height, color):
        self.center_x = x
        self.center_y = y
        self.color = color
        self.width1 = 1000
        self.height1 = 500
        self.width = width
        self.height = height

    def display(self):
        arcade.draw_ellipse_filled(self.center_x, self.center_y, self.width ,self.height , self.color)



