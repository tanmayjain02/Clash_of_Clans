from libraries import *
from king import *

def move_troops(troops , buildings , grid):
    
    for troop1 in troops:
        if troop1.get_health() <= 0:
            continue
        min_dist = 30000000
        target_building = 0

        for i,building in enumerate(buildings):

            if i> (6 + No_of_canon + No_of_wizard - 1):
                break
            if building.get_health() <= 0:
                continue
            dist = abs(building.getx() - troop1.getx()) + abs(building.gety() - troop1.gety())

            if dist < min_dist:
                min_dist = dist
                target_building = building
        
        if min_dist != 30000000:
            troop1.move_troop(target_building , grid , buildings , troops)



class barb(character):
    def __init__(self , x , y , health , damage , speed , color):
        character.__init__(self , x , y , health , speed , color)
        self.damage = damage 
        self.type = "barb"
    
    def getx(self):
        return self.posx
    
    def gety(self):
        return self.posy
    
    def setx(self, x):
        self.posx = x
    
    def sety(self , y):
        self.posy = y
    
    def get_health(self):
        return self.health
    
    def set_health(self , health):
        self.health = health
    
    def get_color(self):
        return self.color
    
    def get_damage(self):
        return self.damage
    
    def set_damage(self , damage):
        self.damage = damage
    
    def show_troop(self , grid):

        x = self.getx()
        y = self.gety()

        if self.health <= 0:
            grid[x][y] = Back.GREEN + " "
            return 

        grid[x][y] = self.color + 'B'
        return grid
    
    def move_troop(self , building , grid , buildings , troops):
        x = self.getx()
        y = self.gety()

        dest_x = building.getx()
        dest_y = building.gety()

        # print(x , y , dest_x , dest_y)

        # If it has to move right
        if dest_y >= y+1:
            x_new = x
            y_new = y+1

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'B'
                # print(self.color)
                # print("HERE", grid[x_new][y_new])
                return
            
            # checking if there is a barbarian at that position
            for troop1 in troops:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'B'
                    # print(self.color)
                    return
                
            for i ,obstacle in enumerate(buildings):
                if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                    obstacle.take_damage(self.damage, grid, i)
                    return
        
        # If it has to move left
        if dest_y <= y-1:
            x_new = x
            y_new = y-1

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'B'
                return
            
            # checking if there is a barbarian at that position
            for troop1 in troops:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'B'
                    # print(self.color)
                    return

                for i ,obstacle in enumerate(buildings):
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                        obstacle.take_damage(self.damage, grid, i)
                        return
                        break
        
        # If it has to move down
        if dest_x >= x+1:
            x_new = x+1
            y_new = y

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'B'
                return
            
            # checking if there is a barbarian at that position
            for troop1 in troops:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'B'
                    # print(self.color)
                    return

                for i ,obstacle in enumerate(buildings):
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                        obstacle.take_damage(self.damage, grid, i)
                        return
                        break
        
        # If it has to move up
        if dest_x <= x-1:
            x_new = x-1
            y_new = y

            if grid[x_new][y_new] == Back.GREEN + " " or grid[x_new][y_new] == self.color + 'B':
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'B'
                return

            # checking if there is a barbarian at that position
            for troop1 in troops:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'B'
                    # print(self.color)
                    return

                for i ,obstacle in enumerate(buildings):
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                        obstacle.take_damage(self.damage, grid, i)
                        return
                        break

        # if (x == dest_x-1 and y == dest_y-1) or (x == dest_x+1 and y == dest_y -1) or (x == dest_x-1 and y == dest_y + 1) or ( x == dest_x +1 and y == dest_y +1):

        
                


