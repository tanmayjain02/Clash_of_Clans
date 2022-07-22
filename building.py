import numpy as np
import colorama
import numpy as np
from colorama import Fore, Back, Style
from building import *
from king import *
colorama.init()
import click
import os
from input import *
from board import *

SCR_HEIGHT = 30
SCR_WIDTH = 60

class building:

    id = 1
    
    def __init__(self , x , y , height , width , health , color):
        self._pos_x = x
        self._pos_y = y
        self._height = height
        self._width = width
        self._health = health
        self.color = color
        self.id = building.id
        building.id  += 1
    
    def get_health(self):
        return self._health
    
    def get_color(self):
        return self._color
    
    def set_color(self , color , index , grid):
        self.color = color 
        self.show(grid)
    
    def getx(self):
        return self._pos_x
    
    def gety(self):
        return self._pos_y
    
    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width

    def get_id(self):
        return self.id 

        self.damage = damag
    def take_damage(self , damage, grid, index):
        self._health -= damage

        if self._health > 50:
            self.color = Fore.GREEN
        elif self._health > 20:
            self.color = Fore.YELLOW
        elif self._health > 0:
            self.color = Fore.RED
        else:
            self.destroy_building(grid)

        self.show(grid)
    
    def destroy_building(self, grid):
        for i in range(self.gety(), self.gety() + self.get_width()):
            for j in range(self.getx() , self.getx() + self.get_height()):
                grid[j][i] = Back.GREEN + ' '
        self._pos_x = -100
        self._pos_y = -100

    def show(self, grid):
        x = self.getx()
        y = self.gety()

        if x <= 0 or y <= 0:
            return

        if self.type == "hut":
            shape = self.hut1
        elif self.type == "castle":
            shape = self.castle1
        elif self.type == "canon":
            shape = self.canon1
        elif self.type == "wall":
            shape = [['X']]
        elif self.type == "wizard_tower":
            shape = [['W']]
            # grid[y][x] = self.color + 'X'
            # return grid
        
        # print(self.get_width() , y , "helllo")
        # print(type(y) , type(self._width) , self._width)

        for i in range(y , y + self._width):
            for j in range(x , x + self._height):
                grid[j][i] = self.color + shape[j-x][i-y]
         
        return grid
                    

class hut(building):

    def __init__(self , x , y , health , color):
        building.__init__(self , x , y , 2 , 3 , health , color)
        self.type = "hut"
    
    def _decrease_hut_health(self , damage):
        self._health -= damage
    
    hut1 = [list("^^^"),
           list("|_|")]
    
    def clear_hut(self , grid):
        x = self.getx()
        y = self.gety()

        # clear the hut from the grid
        for i in range(y , y+2):
            for j in range(x , x + 3):
                grid[i][j] = " "
        
        return grid
    

    
    def show_hut(self , grid):
        x = self.getx()
        y = self.gety()

        # print(x , y)
        # print(len(grid) , len(grid[0]))
        for j in range(y , y+3):
            for i in range(x , x + 2):
                # print(i,j)
                grid[i][j] = self.hut1[i-x][j-y]
        
        return grid
    
    def store_id(self , grid , id):
        x = self.getx()
        y = self.gety()

        for i in range(y , y+2):
            for j in range(x , x+3):
                grid[i][j] = self.id
        
        return grid



class castle(building):
    def __init__(self , x , y , health , color):
        building.__init__(self , x , y ,3 , 5 ,  health , color)
        self.type = "castle"
    
    
    castle1 = [list("/\\_/\\"),
           list("|   |"), 
           list("`````")]
    
    def clear_castle(self , grid):
        x = self.getx()
        y = self.gety()

        # clear the hut from the grid
        for i in range(y , y+3):
            for j in range(x , x + len(5)):
                grid[i][j] = " "
        
        return grid
    
    def show_castle(self , grid):
        x = self.getx()
        y = self.gety()

        for i in range(y , y+3):
            for j in range(x , x+len(self.castle1[i-y])):
                grid[i][j] = self.castle1[i-y][j-x]
        
        return grid
    
    def store_id(self , grid , id):
        x = self.getx()
        y = self.gety()

        for i in range(y , y+3):
            for j in range(x , x+len(self.castle1[i-y])):
                grid[i][j] = self.id
        
        return grid 

class wall(building):
    def __init__(self , x , y , health , color):
        building.__init__(self , x , y ,1 , 1 ,  health , color)
        self.type = "wall"
    
    def show_wall(self , grid):
        x = self.getx()
        y = self.gety()
        grid[y][x] = Fore.BLACK + Back.WHITE + 'X'
        return grid
