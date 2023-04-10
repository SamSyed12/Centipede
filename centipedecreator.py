import arcade
from centipedecompartment import centipede_compartment

class centipede:
    def __init__(self):
            self.centipede_list = []
            while len(self.centipede_list) < 10:
                self.centipede_list.append(centipede_compartment(900 - 20* len(self.centipede_list), 480, 20, arcade.color.YELLOW))



    def display(self):
        for centipede_compartment in self.centipede_list:
            centipede_compartment.display()




