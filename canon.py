from urllib.request import build_opener
from libraries import *
from building import *

class canon(building):
    def __init__(self , x , y , health , color , damage , grid):
        building.__init__(self , x , y , 2 , 3 , health , color)
        self.damage = damage
        self.grid = grid
        self.type = "canon"

    canon1 = [list("| |") , 
              list("|_|")]
    
    def attack(self , user_avatar , troops): # user_avatar = king / queen
        x = self.getx()
        y = self.gety()


        x_up = max(2 , x -5)
        x_down = min(SCR_HEIGHT - 2 , x + 5)
        y_left = max(0 , y-5)
        y_right = min(SCR_WIDTH-2 , y+5)

        # If any king or barb comes in this radius , then attack them

        # Checking for user_avatar
        if x_up <= user_avatar.getx() <= x_down and y_left <= user_avatar.gety() <= y_right :
            if user_avatar.type == 'king':
                # print("No")
                user_avatar.do_damage(5 , self.grid , "king")
            else :
                # print("Yes")
                user_avatar.do_damage(5 , self.grid , "queen")
            return 

        # Checking for troops 
        for troop1 in troops:
            if x_up <= troop1.getx() <= x_down and y_left <= troop1.gety() <= y_right and troop1.type != "balloon":
                print("Canon is working")
                troop1.do_damage(5 , self.grid , troop1.type)
                break
            
