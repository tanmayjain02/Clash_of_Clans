from libraries import *

class attack:
    def __init__(self , x , y , damage , direction ,  buildings, board1):
        self.posx = x
        self.posy = y
        self.damage = damage
        self.direction = direction
        self.grid = board1._grid
        self.id = 0 
        self.board1 = board1
        self.buildings = buildings
        # self.building_posn = building_posn
    
    def getx(self):
        return self.posx
    
    def gety(self):
        return self.posy

    def check_attack_possible(self):
        x = self.getx()
        y = self.gety()

        if self.direction == 'up':
            x -= 1
        elif self.direction == 'down':
            x += 1
        elif self.direction == 'left':
            y -= 1
        elif self.direction == 'right':
            y += 1

        # print(x,y)

        for i, building in enumerate(self.buildings):
            if building.getx() <= x < building.getx() + building.get_height() and building.gety() <= y < building.gety() + building.get_width():
                building.take_damage(self.damage, self.grid, i)
                break


