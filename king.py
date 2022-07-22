from numpy import FPE_OVERFLOW
from colorama import *
from libraries import *
import time

SCR_HEIGHT = 30
SCR_WIDTH = 60

class character:
    def __init__(self , x , y , health , speed , color):
        self.posx = x
        self.posy = y
        self.health = health
        self.speed = speed
        self.is_dead = False
        self.color = color
        self.direction = "right"

    def getx(self):
        return self.posx
    
    def setx(self , x):
        self.posx = x
    
    def gety(self):
        return self.posy
    
    def sety(self , y):
        self.posy = y
    
    def get_health(self):
        return self.health
    
    def set_health(self , health):
        self.health = health
    
    def get_speed(self):
        return self.speed
    
    def set_speed(self , speed):
        self.speed = speed
    
    def do_damage(self , damage , grid , type):

        global balloon_num , archer_num , barb_num
        print(barb_num , archer_num , balloon_num)

        self.set_health(self.get_health() -damage)

        if self.get_health() > 50:
            self.color = Fore.GREEN
        elif self.get_health() > 20:
            self.color = Fore.YELLOW
        elif self.get_health() > 0:
            self.color = Fore.RED
        
        if self.get_health() <= 0:    
            if self.type == "balloon":
                balloon_num = balloon_num - 1        
            elif self.type == "archer":
                archer_num = archer_num - 1
            elif self.type == "barb":
                barb_num = barb_num - 1
                # print("Reached here" , barb_num)        
        
        self.show(grid , type)
    
    def show(self , grid , type):
        x = self.getx()
        y = self.gety()

        if self.type != "king" and self.type != "queen"  and self.get_health() <= 0:
            grid[x][y] = Back.GREEN + " " 
            self.setx(-100)
            self.sety(-100)
            return grid
        
        if self.get_health() <= 0:
            self.setx(-100)
            self.sety(-100)

        if x<=0 or y<= 0:
            return 

        if type == "king":
            grid[x][y] = self.color + 'K'
        elif type == "queen":
            grid[x][y] = self.color + 'Q'
        elif type == "archer":
            grid[x][y] = self.color + 'a'
        elif type == "balloon":
            grid[x][y] == self.color + 'q'
        else:
            grid[x][y] = self.color + 'B'
        
        return grid

class king(character):
    def __init__(self , x , y , health , speed , color):
        character.__init__(self , x , y , health , speed , color)
        self.type = "king"
    
    def show_king(self , grid):
        x = self.getx()
        y = self.gety()

        grid[x][y] = self.color + 'K'
        return grid
    
    def clear_king(self , grid):
        x = self.getx()
        y = self.gety()

        grid[x][y] = Back.GREEN + " "
        return grid
    
    # Functions to move king 
    def move_up(self , grid):
        x = self.getx()
        y = self.gety()

        if x-1 > 0 and grid[x-1][y] == (Back.GREEN + " "):
            self.setx(x-1)
            grid[x][y] = Back.GREEN + " "
            grid[x-1][y] = self.color + 'K' 
        
        return grid
    
    def move_down(self , grid):
        x = self.getx()
        y = self.gety()

        if x+1 < SCR_HEIGHT and grid[x+1][y] == (Back.GREEN + " "):
            self.setx(x+1)
            grid[x][y] = Back.GREEN + " "
            grid[x+1][y] = self.color + 'K'
        
        return grid
    
    def move_left(self , grid):
        x = self.getx()
        y = self.gety()

        if y-1 > 0 and grid[x][y-1] == (Back.GREEN + " "):
            self.sety(y-1)
            grid[x][y] = Back.GREEN + " "
            grid[x][y-1] = self.color + 'K'
        
        return grid

    def move_right(self , grid):
        x = self.getx()
        y = self.gety()

        if y+1 < SCR_WIDTH and grid[x][y+1] == (Back.GREEN + " "):
            self.sety(y+1)
            grid[x][y] = Back.GREEN + " "
            grid[x][y+1] = self.color + 'K'
        
        return grid
    
    