from urllib.request import build_opener
from libraries import *
from building import *

# Can attack aerial troops 
class wizard_tower(building):
    def __init__(self , x , y , health , color , damage , grid):
        building.__init__(self , x , y , 1 , 1 , health , color)
        self.damage = damage
        self.grid = grid
        self.type = "wizard_tower"
    
    def attack(self , user_avatar , troops):
        x = self.getx()
        y = self.gety()

        x_up = max(2 , x -5)
        x_down = min(SCR_HEIGHT - 2 , x + 5)
        y_left = max(0 , y-5)
        y_right = min(SCR_WIDTH-2 , y+5)

        x_target = -1
        y_target = -1

        if x_up <= user_avatar.getx() <= x_down and y_left <= user_avatar.gety() <= y_right:
            x_target = user_avatar.getx()
            y_target = user_avatar.gety()

        # If any troop comes in this radius , then attack them 
        for troop1 in troops:
            if x_up <= troop1.getx() <= x_down and y_left <= troop1.gety() <= y_right:
                x_target = troop1.getx()
                y_target = troop1.gety()
                # troop1.do_damage(5 , self.grid , "troop1")
                break
        
        x_cord = [x_target -1 , x_target , x_target+1]
        y_cord = [y_target -1 , y_target , y_target+1]

        for a in x_cord:
            for b in y_cord:
                for troop1 in troops:
                    if troop1.getx() == a and troop1.gety() == b:
                        print("Wizard tower is working")
                        troop1.do_damage(5 , self.grid , troop1.type)
        
        if x_up <= user_avatar.getx() <= x_down and y_left <= user_avatar.gety() <= y_right:
            if user_avatar.type == 'king':
                print("Wizard is attacking king")
                user_avatar.do_damage(5 , self.grid , "king")
            else :
                print("Wizard is attacking queen")
                user_avatar.do_damage(5 , self.grid , "queen")
            
