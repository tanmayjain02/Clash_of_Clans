import enum
import imp
import colorama
import numpy as np
from colorama import Fore, Back, Style
from building import *
from king import *
colorama.init()
from libraries import *
import os
from input import *
from attack import *
from board import *
from canon import *
# from troop import *
from troopFile import troop, move_troops
import time
import os

starttime = time.time()

def clrscr():
   # Clear screen using click.clear() function
    click.clear()


        
board1 = board(SCR_HEIGHT, SCR_WIDTH)

# Making a array containing building positions
building_posn = [[10 , 10] , [22 , 16] , [22 , 10] , [22 , 22] , [10 , 26] , [15 , 35]]
buildings = []

# Create 5 huts
for i in range(0 , 5):
    buildings.append(hut(building_posn[i][0] , building_posn[i][1] , 100 , Fore.BLUE))
    board1._grid = buildings[i].show_hut(board1._grid)

# Create  a town hall
buildings.append(castle(building_posn[5][0] , building_posn[5][1] , 100 , Fore.BLUE))
board1._grid = buildings[5].show(board1._grid)

# # Create two canons
canon_posn = [[15 , 28] , [15 , 45]]

index = 6
for i in range(0 , 2):
    canon1 = (canon(canon_posn[i][0] , canon_posn[i][1] , 100 , Fore.YELLOW + Back.LIGHTBLUE_EX , 5 ,board1._grid))
    buildings.append(canon1)
    board1._grid = canon1.show(board1._grid)
    index += 1

# Create walls
index = 6
for i in range(5 , SCR_WIDTH-5):
    # building_posn.append([i , 5])
    buildings.append(wall(5 , i , 100 , Fore.BLACK + Back.WHITE))
    board1._grid = buildings[index].show(board1._grid)
    index += 1

for i in range(5 , SCR_WIDTH-5):
    # building_posn.append([i , SCR_HEIGHT-5])
    buildings.append(wall(SCR_HEIGHT-5 , i , 100 , Fore.BLACK + Back.WHITE))
    board1._grid = buildings[index].show(board1._grid)
    index += 1

for i in range(5 , SCR_HEIGHT-5):
    buildings.append(wall(i , 5 , 100 , Fore.BLACK + Back.WHITE))
    board1._grid = buildings[index].show(board1._grid)
    index += 1

for i in range(5 , SCR_HEIGHT-4):
    buildings.append(wall(i, SCR_WIDTH-5 , 100 , Fore.BLACK + Back.WHITE))
    board1._grid = buildings[index].show(board1._grid)
    index += 1



# Create a king
king1 = king(1 , 1 , 100 , 3 , Back.BLACK + Fore.LIGHTYELLOW_EX)

# Display the king
board1._grid = king1.show_king(board1._grid)
board1.display_grid()

# Stores the troops/barbs
troops = []

c_flag = 0
r_flag = 0 # Rage spell
h_flag = 0 # healing spell

if __name__ == "__main__":
    replay_input = []
    # ask name of game
    name = input("pls input name of the file")

    input_array = []
    if os.path.exists(name):
        with open(name , "r") as f:
            # for i in f:
            #     input_array.append(i)
            while 1:
                char = f.read(1)
                if not char:
                    break
                input_array.append(char)
        
        t = 0.1

    for ch in input_array:
        print(ch)
        # if ch == " ":
            # print("hi")
        time.sleep(t)
    # Check for victory 
        vict_flag = 1
        lost_flag = 1

        for i,building in enumerate(buildings):

            if i > 7:
                break
            if building.getx() != -100:
                vict_flag = 0
        
        if vict_flag == 1:
            os.system("clear")
            victory = [list("\\    / | |'''  '''''' |'''| |'''| \\  /"),
                       list(" \\  /  | |        |   |   | |,,,|  \\/"), 
                       list("  \\/   | |,,,     |   |...| |  \    ||")]
            # for i in victory:
            #     print(i) 
            print("Yay , you won the game")
            # make_replay(replay_input)


            break
        
        if king1.get_health() > 0:
            lost_flag = 0
        for troop1 in troops:
            if troop1.get_health():
                lost_flag = 0
        
        if lost_flag == 1:
            os.system("clear")
            print("You lost :>")
            # make_replay(replay_input)
            break
        
        if(time.time() - starttime >= 1.0):
            c_flag = 1-c_flag
        
            if c_flag==1:
                buildings[6].set_color(Fore.RED , 6 , board1._grid) # canon1 
                buildings[7].set_color(Fore.RED , 7  , board1._grid) # canon2
                buildings[6].attack(king1 , troops)
                buildings[7].attack(king1 , troops)
            else:
                buildings[6].set_color(Fore.YELLOW , 6 , board1._grid) # canon1 
                buildings[7].set_color(Fore.YELLOW , 7 , board1._grid) # canon2
                buildings[6].attack(king1 , troops)
                buildings[7].attack(king1 , troops)
            
            starttime = time.time()


        if r_flag == 1:
            val = input_to(Get(),0.05)
        else:
            val = input_to(Get() , 0.1)
        replay_input.append(val)

        os.system("clear")
        board1.display_grid()
        if king1.get_health() <= 0:
            print("King is dead :(")
        else :
            health = king1.get_health()
            num_of_tiles = round(health/100 * 10)
        
            if health > 50:
                for i in range(num_of_tiles):
                    print(Fore.GREEN + "|" + Style.RESET_ALL , end = "")
                print()
                # print('ye')
            elif health > 20:
                for i in range(num_of_tiles):
                    print(Fore.YELLOW + "|" + Style.RESET_ALL , end = "")
                print()
            else:
                for i in range(num_of_tiles):
                    print(Fore.RED + "|" + Style.RESET_ALL , end = "")
                print()

        val = ch
        if(val == 'q' or val == 'Q'):
            break

        elif(val == 'w' or val == 'W'):
            if(king1.get_health()<=0):
                continue
            board1._grid = king1.move_up(board1._grid)
            king1.direction = "up"
            # os.system("clear")
            # board1.display_grid()

        elif(val == 'a' or val == 'A'):
            if(king1.get_health()<=0):
                continue
            board1._grid = king1.move_left(board1._grid)
            king1.direction = "left"
            # os.system("clear")
            # board1.display_grid()

        elif(val == 's' or val == 'S'):
            if(king1.get_health()<=0):
                continue
            board1._grid = king1.move_down(board1._grid)
            king1.direction = "down"
            # os.system("clear")
            # board1.display_grid()

        elif(val == 'd' or val == 'D'):
            if(king1.get_health()<=0):
                continue
            board1._grid = king1.move_right(board1._grid)
            king1.direction = "right"
            # os.system("clear")
            # board1.display_grid()
        
        elif(val == ' '):
            attack1 = attack(king1.getx()  , king1.gety() , 10 , king1.direction , building_posn , buildings , board1)
            attack1.check_attack_possible()
        
        elif(val == '1'):
            troop1 = troop(1 ,5 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK )
            troop1.show_troop(board1._grid)
            troops.append(troop1)

        elif(val == '2'):
            troop1 = troop(1 ,6 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            troops.append(troop1)

        elif(val == '3'):
            troop1 = troop(1 ,7 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            troops.append(troop1)
        
        elif(val == 'r' or val == 'R'):
            r_flag = 1
            t = 0.05
        elif(val == 'h' or val == 'H'):
            # Increase health of king
            king1.set_health(max(100 , 1.5*king1.get_health()))
            #Increase health of all troops
            for troop1 in troops:
                troop1.set_health(max(20 , 1.5*troop1.get_health()))

        # print("hi")
        move_troops(troops , buildings , board1._grid)
            