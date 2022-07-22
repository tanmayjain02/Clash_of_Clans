import re
from libraries import *
from king import *


def move_balloons(balloons, buildings, grid, defensive_building):

    for troop1 in balloons:
        if troop1.get_health() <= 0:
            continue
        min_dist = 30000000
        target_building = 0

        # Check for defensive buildings
        for i, building in enumerate(defensive_building):

            if building.get_health() <= 0:
                continue
            dist = abs(building.getx() - troop1.getx()) + \
                abs(building.gety() - troop1.gety())

            if dist < min_dist:
                min_dist = dist
                target_building = building

        if min_dist != 30000000:
            # print("Defn", target_building.type)
            # print(len(defensive_building))
            troop1.move_balloon(target_building, grid, buildings, balloons)
            continue

        for i, building in enumerate(buildings):

            if i > (6 + No_of_canon + No_of_wizard - 1):
                break
            if building.get_health() <= 0:
                continue
            dist = abs(building.getx() - troop1.getx()) + \
                abs(building.gety() - troop1.gety())

            if dist < min_dist:
                min_dist = dist
                target_building = building

        if min_dist != 30000000:
            print(target_building.type)
            troop1.move_balloon(target_building, grid, buildings, balloons)


class balloon(character):

    def __init__(self, x, y, health, damage, speed, color):
        character.__init__(self, x, y, health, speed, color)
        self.damage = damage

        self.prev_tile = self.color + 'q'
        self.type = "balloon"

    def getx(self):
        return self.posx

    def gety(self):
        return self.posy

    def setx(self, x):
        self.posx = x

    def sety(self, y):
        self.posy = y

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_color(self):
        return self.color

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

    def show_troop(self, grid):

        x = self.getx()
        y = self.gety()

        if self.health <= 0:
            grid[x][y] = Back.GREEN + " "
            return

        grid[x][y] = self.color + 'q'
        return grid

    def move_balloon(self, building, grid, buildings, troops):
        x = self.getx()
        y = self.gety()

        dest_x = building.getx()
        dest_y = building.gety()

        # print("x is", x, "y is ", y)
        # print("x_dest is ", dest_x, "dest_y is ", dest_y)

        # If it has to move right
        if dest_y >= y+1:
            x_new = x
            y_new = y+1

            # if grid[x_new][y_new] == Back.GREEN + " ":
            self.setx(x_new)
            self.sety(y_new)
            grid[x][y] = Back.GREEN + " "
            # self.prev_tile = grid[x_new][y_new]
            grid[x_new][y_new] = self.color + 'q'

        # If it has to move left
        elif dest_y <= y-1:
            x_new = x
            y_new = y-1

            self.setx(x_new)
            self.sety(y_new)
            grid[x][y] = Back.GREEN + " "
            # self.prev_tile = grid[x_new][y_new]
            grid[x_new][y_new] = self.color + 'q'

        # If it has to move down
        elif dest_x >= x+1:
            x_new = x+1
            y_new = y

            self.setx(x_new)
            self.sety(y_new)
            grid[x][y] = Back.GREEN + " "
            # self.prev_tile = grid[x_new][y_new]
            grid[x_new][y_new] = self.color + 'q'

        # If it has to move up
        elif dest_x <= x-1:
            x_new = x-1
            y_new = y

            self.setx(x_new)
            self.sety(y_new)
            grid[x][y] = Back.GREEN + " "
            # self.prev_tile = grid[x_new][y_new]
            grid[x_new][y_new] = self.color + 'q'

        else:
            for i, obstacle in enumerate(buildings):
                if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                    obstacle.take_damage(self.damage, grid, i)
