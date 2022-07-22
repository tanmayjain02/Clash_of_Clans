from libraries import *

class board:

    def __init__(self , height , width):
        # Make a grid of passed dimension
        self._height = height
        self._width = width 

        # Will store the object of buildings
        self.buildings = []

        self._grid = [[" " for i in range(width)] for i in range(height)]

        # making a pseudo grid to know what is present where
        self._bggrid = [[0 for i in range(width)] for i in range(height)]
        
        self._color_board()
        self._make_border()


    def _make_border(self):
        for i in range(self._width):
            self._grid[0][i] = Back.RED + Fore.BLUE + "T" 
            self._grid[self._height -1][i] = Back.RED + Fore.BLUE + "T" 
        
        for i in range(self._height):
            self._grid[i][0] = Back.RED + Fore.BLUE + "T"
            self._grid[i][self._width - 1] = Back.RED + Fore.BLUE + "T" 
    
    def _color_board(self):
        for i in range(self._width):
            for j in range(self._height):
                self._grid[j][i] = Back.GREEN + " "


    def display_grid(self):
        for i in range(self._height):
            for j in range(self._width):
                print(self._grid[i][j] +  Style.RESET_ALL , end = "")
            print()

    def get_building(self , id):
        for building in self.buildings:
            if building.get_id() == id:
                return building
    
    def change_board(self , x , y , value):
        self._grid[x][y]