import arcade
from firing_position import firing_position
from random import randint
from particle2 import torpedo
from rockss import rocks
from centipedecreator import centipede
from math import sqrt


def dist(item1, item2):
    return sqrt((item2.center_x - item1.center_x)**2 + (item2.center_y - item1.center_y)**2)

class Main(arcade.Window):
    def __init__(self, w, h, title):
        super().__init__(w, h, title)
        self.shoota = firing_position(randint(300, 600), 50)
        self.moving_left_shoota = False
        self.moving_right_shoota = False
        self.torpedo_list = []
        self.shoot = True
        self.obstacle_list = []
        self.particle_list = []
        self.centipede = centipede()
        self.score = 0
        self.end = False
        self.start = True
        self.display_firing_position = True
        self.display_centipede = True

        while len(self.obstacle_list) < 25:
            self.obstacle_list.append(rocks(randint(40, 960), randint(90, 460), 15, 15, arcade.color.BATTLESHIP_GREY))

    def on_draw(self):
        self.clear()
        self.shoota.returntocentre()
        self.torpedo_collision_obstacle()
        self.cent_collision_obstacle()
        self.cent_collision_torpedo()
        self.cent_collision_shoota()
        self.end_sequence()

        if self.display_centipede == True:
            self.centipede.display()
        if self.display_firing_position == True:
            self.shoota.display()
        if self.moving_right_shoota == True:
            self.shoota.turnright()
        if self.moving_left_shoota == True:
            self.shoota.turnleft()
        for torpedo in self.torpedo_list:
            torpedo.display()
        for rocks in self.obstacle_list:
            rocks.display()


        arcade.draw_text("SCORE:" + str(self.score), 40, 50, arcade.color.WHITE_SMOKE, 20, 50 ,  "right", "calibri", False )

    def torpedo_collision_obstacle(self):
        if self.start == True:



            for i in range(len(self.torpedo_list)-1, -1, -1):
                x = self.torpedo_list[i]

                hit = False

                if x.center_y < 0 or x.center_y > 500:
                    del(self.torpedo_list[i])


                for g in range(len(self.obstacle_list) - 1, -1, -1):
                    y = self.obstacle_list[g]
                    if dist(y, x) < y.width/2 + x.size/2:
                        hit = True
                        del(self.obstacle_list[g])
                        self.score +=1

                if hit == True:
                    del(self.torpedo_list[i])


    def cent_collision_obstacle(self):
        if self.start == True:

            for g in range(len(self.centipede.centipede_list) -1, -1, -1):
                y = self.centipede.centipede_list[g]

                for i in range(len(self.obstacle_list)-1, -1, -1):
                    x = self.obstacle_list[i]
                    if dist(y, x) < x.width/2 + y.size/2:
                        self.centipede.centipede_list[g].x_dir *= -1
                        self.centipede.centipede_list[g].center_y -= y.size + 1

    def cent_collision_torpedo(self):
        if self.start == True:
            for g in range(len(self.centipede.centipede_list) -1, -1, -1):
                y = self.centipede.centipede_list[g]

                for i in range(len(self.torpedo_list)-1, -1, -1):
                    x = self.torpedo_list[i]
                    if dist(y, x) < x.size/2 + y.size/2:
                        del(self.centipede.centipede_list[g])
                        del(self.torpedo_list[i])
                        self.obstacle_list.append(rocks(y.center_x, y.center_y, randint(15, 20), randint(15, 20), arcade.color.BATTLESHIP_GREY))
                        self.score += 1
                        if len(self.centipede.centipede_list) == 0:
                            self.end = True

    def cent_collision_shoota(self):
        if self.start == True:
            for g in range(len(self.centipede.centipede_list)-1, -1, -1):
                y = self.centipede.centipede_list[g]
                x = self.shoota
                if dist(y, x) < y.size/2 + x.width/2:
                    self.end = True
                    self.display_firing_position = False
                    self.display_centipede = False


    def end_sequence(self):
        if self.end == True:
            self.start = False
            arcade.draw_text("GAME OVER", 360, 250, arcade.color.RED, 36)
            arcade.draw_text("FINAL SCORE:" + str(self.score), 360, 200, arcade.color.WHITE, 28)


    def on_key_press(self, symbol: int, modifiers: int):
        if self.start == True:

            if symbol == arcade.key.LEFT:
                self.moving_left_shoota = True

            if symbol == arcade.key.RIGHT:
                self.moving_right_shoota = True

            if symbol == arcade.key.SPACE:
                if self.shoot == True:
                    self.torpedo_list.append(torpedo(self.shoota.center_x, self.shoota.center_y + 25, 4, 10, 0, 1, arcade.color.WHITE))


    def on_key_release(self, symbol: int, modifiers: int):
            if symbol == arcade.key.LEFT:
                self.moving_left_shoota = False

            if symbol == arcade.key.RIGHT:
                self.moving_right_shoota = False


arcade.window = Main(1000, 500, "Centipede")
arcade.run()


