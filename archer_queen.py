from king import *
from libraries import *

class queen(character):
    def __init__(self , x , y , health , speed , color):
        character.__init__(self , x , y , health , speed , color)
        self.type = "queen"
    
    def show_queen(self , grid):
        x = self.getx()
        y = self.gety()

        grid[x][y] = self.color + 'Q'
        return grid
    
    def clear_queen(self , grid):
        x = self.getx()
        y = self.gety()

        grid[x][y] = Back.GREEN + " "
        return grid
    
    # Functions to move queen 
    def move_up(self , grid):
        x = self.getx()
        y = self.gety()

        if x-1 > 0 and grid[x-1][y] == (Back.GREEN + " "):
            self.setx(x-1)
            grid[x][y] = Back.GREEN + " "
            grid[x-1][y] = self.color + 'Q' 
        
        return grid
    
    def move_down(self , grid):
        x = self.getx()
        y = self.gety()

        if x+1 < SCR_HEIGHT and grid[x+1][y] == (Back.GREEN + " "):
            self.setx(x+1)
            grid[x][y] = Back.GREEN + " "
            grid[x+1][y] = self.color + 'Q'
        
        return grid
    
    def move_left(self , grid):
        x = self.getx()
        y = self.gety()

        if y-1 > 0 and grid[x][y-1] == (Back.GREEN + " "):
            self.sety(y-1)
            grid[x][y] = Back.GREEN + " "
            grid[x][y-1] = self.color + 'Q'
        
        return grid

    def move_right(self , grid):
        x = self.getx()
        y = self.gety()

        if y+1 < SCR_WIDTH and grid[x][y+1] == (Back.GREEN + " "):
            self.sety(y+1)
            grid[x][y] = Back.GREEN + " "
            grid[x][y+1] = self.color + 'Q'
        
        return grid
    
    def attack(self , damage , buildings , board1):
        x = self.getx()
        y = self.gety()

        target_x = -1
        target_y = -1

        if self.direction == 'up':
            target_x = x - 8
            target_y = y
        elif self.direction == 'down':
            target_x = x + 8
            target_y = y
        elif self.direction == 'right':
            target_x = x
            target_y = y + 8
        elif self.direction == 'left':
            target_x = x
            target_y = y-8
        
        x_cord = [target_x -2 , target_x -1 , target_x , target_x +1 , target_x + 2]
        y_cord = [target_y -2 , target_y -1 , target_y , target_y +1 , target_y + 2]

        for a in x_cord:
            for b in y_cord:
                # Check if any building is present at (a,b) , if yes then do damage to it
                for i, building in enumerate(buildings):
                    if building.getx() <= a < building.getx() + building.get_height() and building.gety() <= b < building.gety() + building.get_width():
                        building.take_damage(damage, board1._grid, i)
                        break

        

        