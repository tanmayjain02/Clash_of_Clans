from libraries import *
from king import *

# The range of the archers is 4 tiles

def move_archers(archers , buildings , grid):
    
    for troop1 in archers:
        if troop1.get_health() <= 0:
            continue
        min_dist = 30000000
        target_building = 0

        for i,building in enumerate(buildings):

            # Replace 7 with the number of non-wall buildings # Change
            if i> (6 + No_of_canon + No_of_wizard - 1):
                break
            if building.get_health() <= 0:
                continue
            dist = abs(building.getx() - troop1.getx()) + abs(building.gety() - troop1.gety())

            if dist < min_dist:
                min_dist = dist
                target_building = building
        
        if min_dist != 30000000:
            # print(target_building.type)
            troop1.move_troop(target_building , grid , buildings , archers)



class archer(character):
    def __init__(self , x , y , health , damage , speed , color):
        character.__init__(self , x , y , health , speed , color)
        self.damage = damage 

        self.type = "archer"
    
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

        grid[x][y] = self.color + 'A'
        return grid
    
    def move_troop(self , building , grid , buildings , archers):
        x = self.getx()
        y = self.gety()

        dest_x = building.getx()
        dest_y = building.gety()

        # print("x is " , x , "y is " , y)
        # print("dest_x is " , dest_x , "dest_y is " , dest_y)

        # If it has to move right
        if dest_y >= y+4:
            x_new = x
            y_new = y+1

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'A'
                return
            
            # checking if there is a archer at that position
            for troop1 in archers:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'A'
                    return

            # Check if any building is in the range of the archer , if yes then attack it    
            for i ,obstacle in enumerate(buildings):
                x_cord = [x_new -4 , x_new-3 , x_new-2 , x_new-1 , x_new , x_new+1 , x_new+2 , x_new+3 , x_new+4]
                y_cord = [y_new -4 , y_new-3 , y_new-2 , y_new-1 , y_new , y_new+1 , y_new+2 , y_new+3 , y_new+4]

                if i <= (6 + No_of_canon + No_of_wizard - 1):
                    for x in x_cord:
                        for y in y_cord:
                            if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                                obstacle.take_damage(self.damage, grid, i)
                                # print("right1\n")
                                return
                else :
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                            obstacle.take_damage(self.damage, grid, i)
                            return
        
        # If it has to move left
        elif dest_y <= y-4:
            x_new = x
            y_new = y-1

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'A'
                return
            
            # checking if there is a barbarian at that position
            for troop1 in archers:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'A'
                    # print(self.color)
                    return

            for i ,obstacle in enumerate(buildings):
                x_cord = [x_new -4 , x_new-3 , x_new-2 , x_new-1 , x_new , x_new+1 , x_new+2 , x_new+3 , x_new+4]
                y_cord = [y_new -4 , y_new-3 , y_new-2 , y_new-1 , y_new , y_new+1 , y_new+2 , y_new+3 , y_new+4]

                if i <= (6 + No_of_canon + No_of_wizard - 1):
                    for x in x_cord:
                        for y in y_cord:
                            if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                                obstacle.take_damage(self.damage, grid, i)
                                # print("left1\n")
                                return
                else :
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                            obstacle.take_damage(self.damage, grid, i)
                            # print("left2\n")
                            return
        
        # If it has to move down
        elif dest_x >= x+4:
            x_new = x+1
            y_new = y

            if grid[x_new][y_new] == Back.GREEN + " ":
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'A'
                return
            
            # checking if there is a barbarian at that position
            for troop1 in archers:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'A'
                    # print(self.color)
                    return

            for i ,obstacle in enumerate(buildings):
                x_cord = [x_new -4 , x_new-3 , x_new-2 , x_new-1 , x_new , x_new+1 , x_new+2 , x_new+3 , x_new+4]
                y_cord = [y_new -4 , y_new-3 , y_new-2 , y_new-1 , y_new , y_new+1 , y_new+2 , y_new+3 , y_new+4]

                if i <= (6 + No_of_canon + No_of_wizard - 1):
                    for x in x_cord:
                        for y in y_cord:
                            if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                                obstacle.take_damage(self.damage, grid, i)
                                # print("down1\n")
                                return
                else :
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                            obstacle.take_damage(self.damage, grid, i)
                            # print("down2\n")
                            return
        
        # If it has to move up
        elif dest_x <= x-4:
            x_new = x-1
            y_new = y

            if grid[x_new][y_new] == Back.GREEN + " " or grid[x_new][y_new] == self.color + 'A':
                self.setx(x_new)
                self.sety(y_new)
                grid[x][y] = Back.GREEN + " "
                grid[x_new][y_new] = self.color + 'A'
                return

            # checking if there is a barbarian at that position
            for troop1 in archers:
                if troop1.getx() == x_new and troop1.gety() == y_new:
                    self.setx(x_new)
                    self.sety(y_new)
                    grid[x][y] = Back.GREEN + " "
                    grid[x_new][y_new] = self.color + 'A'
                    return

            for i ,obstacle in enumerate(buildings):
                x_cord = [x_new -4 , x_new-3 , x_new-2 , x_new-1 , x_new , x_new+1 , x_new+2 , x_new+3 , x_new+4]
                y_cord = [y_new -4 , y_new-3 , y_new-2 , y_new-1 , y_new , y_new+1 , y_new+2 , y_new+3 , y_new+4]

                if i <= (6 + No_of_canon + No_of_wizard - 1):
                    for x in x_cord:
                        for y in y_cord:
                            if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                                obstacle.take_damage(self.damage, grid, i)
                                # print("up1\n")
                                return
                else :
                    if obstacle.getx() <= x_new < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y_new < obstacle.gety() + obstacle.get_width():
                            obstacle.take_damage(self.damage, grid, i)
                            # print("up2\n")
                            return
        
        else:

        # Check if any building is in the range of the archer , if yes then attack it    
            for i ,obstacle in enumerate(buildings):
                x_cord = [x -4 , x-3 , x-2 , x-1 , x , x+1 , x+2 , x+3 , x+4]
                y_cord = [y -4 , y-3 , y-2 , y-1 , y , y+1 , y+2 , y+3 , y+4]

                if i <= (6 + No_of_canon + No_of_wizard - 1):
                    for x in x_cord:
                        for y in y_cord:
                            if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                                obstacle.take_damage(self.damage, grid, i)
                                return
                else :
                    if obstacle.getx() <= x < obstacle.getx() + obstacle.get_height() and obstacle.gety() <= y < obstacle.gety() + obstacle.get_width():
                        obstacle.take_damage(self.damage, grid, i)
                        return
    


        
                
