import enum
import imp
from shutil import move
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
from archer import *
from balloon import *
from archer_queen import *
from wizard_tower import *
import time 


# Take if there is king or queen in the game

type = input("type k for king and q for queen")

# from troop import *
from troopFile import barb, move_troops
import time

starttime = time.time()

def clrscr():
   # Clear screen using click.clear() function
    click.clear()

def make_replay(replay_input):
    name = input("with what name you want to save this game")

    # print(replay_input)

    with open(name , "w") as f:
        for val in replay_input:
            if val != None:
                f.write(val)
            else :
                f.write("x")
    
def make_game_level(level , board1 , user_avatar , buildings , troops , barbs , archers , balloons , canons , wizard_towers , walls , defensive_building):

    global No_of_canon , No_of_wizard
    global barb_num , archer_num , balloon_num
    # Reset the troop numbers
    barb_num = 0
    archer_num = 0
    balloon_num = 0

    # Update the number of canon and wizard 
    if level == 2:
        No_of_canon = 3
        No_of_wizard = 3
    
    if level == 3:
        No_of_canon = 4
        No_of_wizard = 4

    # Clear the grid 
    for i in range(board1._width):
        for j in range(board1._height):
            board1._grid[j][i] = Back.GREEN + " "
    
    # Empty the buildings list , troops , balloons , canon , wizard_tower list
    buildings.clear()
    walls.clear()
    troops.clear()
    balloons.clear()
    barbs.clear()
    archers.clear()
    canons.clear()
    wizard_towers.clear()

    # Create 5 huts
    building_posn = [[18 , 10] , [18 , 14], [18 , 18], [22 , 10] , [22 , 14] , [15 , 35]]
    for i in range(0 , 5):
        buildings.append(hut(building_posn[i][0] , building_posn[i][1] , 100 , Fore.BLUE))
        board1._grid = buildings[i].show_hut(board1._grid)
    
    # Create town hall
    buildings.append(castle(building_posn[5][0] , building_posn[5][1] , 100 , Fore.BLUE))
    board1._grid = buildings[5].show(board1._grid)

    # Update king/Queen

    user_avatar.posx = 1
    user_avatar.posy = 1
    user_avatar.health = 100
    user_avatar.color = Back.BLACK + Fore.LIGHTYELLOW_EX


    canon_posn = [[15 , 28] , [15 , 45] , [15 , 24] , [12 , 26]]
    # Place canons as per Level number
    for i in range(0 , No_of_canon):
        canon1 = (canon(canon_posn[i][0] , canon_posn[i][1] , 100 , Fore.YELLOW + Back.LIGHTBLUE_EX , 5 ,board1._grid))
        buildings.append(canon1)
        canons.append(canon1)
        defensive_building.append(canon1)
        canon1.show(board1._grid)

    wizard_posn = [[8 , 16] , [9 , 16] , [11, 16] , [12 , 16]]
    # Place wizard tower as per level number
    for i in range(No_of_wizard):
        wizard = wizard_tower(wizard_posn[i][0] , wizard_posn[i][1] , 100 , Fore.BLUE , 5 , board1._grid)
        buildings.append(wizard)
        defensive_building.append(wizard)
        wizard_towers.append(wizard)
        wizard.show(board1._grid)

    # Create walls
    wall_index = 0
    for i in range(5 , SCR_WIDTH-5):
        temp_wall = wall(5 , i , 100 , Fore.BLACK + Back.WHITE)
        buildings.append(temp_wall)
        walls.append(temp_wall)
        walls[wall_index].show(board1._grid)
        wall_index += 1

    for i in range(5 , SCR_HEIGHT-5):
        temp_wall = wall(i, SCR_WIDTH-5 , 100 , Fore.BLACK + Back.WHITE)
        buildings.append(temp_wall)
        walls.append(temp_wall)
        walls[wall_index].show(board1._grid)
        wall_index += 1

    for i in range(5 , SCR_WIDTH-5):
        # building_posn.append([i , SCR_HEIGHT-5])
        temp_wall = wall(SCR_HEIGHT-5 , i , 100 , Fore.BLACK + Back.WHITE)
        buildings.append(temp_wall)
        walls.append(temp_wall)
        walls[wall_index].show(board1._grid)
        wall_index += 1


    for i in range(5 , SCR_HEIGHT-5):
        temp_wall = wall(i , 5 , 100 , Fore.BLACK + Back.WHITE)
        buildings.append(temp_wall)
        walls.append(temp_wall)
        walls[wall_index].show(board1._grid)
        wall_index += 1

    if level == 1:
        # reset the health of king/ queen and place it back to (1 , 1)
        print("Level1")
    elif level == 2:
        print("level 2")
    if level == 3:
        print("level3") 


#################
#### Main #######
#################

board1 = board(SCR_HEIGHT, SCR_WIDTH)

# Making a array containing building positions
buildings = []
walls = []
# Store all kind of troop 
troops = []
barbs = []
archers = []
balloons = []
# Buildings list 
canons = []
wizard_towers = []
walls = []
defensive_building = []

# Create a king or queen depending on the type
king1 = king(1 , 1 , 100 , 3 , Back.BLACK + Fore.LIGHTYELLOW_EX)
queen1 = queen(1 , 1 , 100 , 3 , Back.BLACK + Fore.LIGHTYELLOW_EX)

# Make game for level 1 
if type == 'k':
    make_game_level(game_level , board1 , king1 , buildings , troops , barbs , archers , balloons , canons , wizard_towers , walls , defensive_building)
else:
    make_game_level(game_level , board1 , queen1 , buildings , troops , barbs , archers , balloons , canons , wizard_towers , walls , defensive_building)

board1.display_grid()
# print(len(buildings) , len(archers) , len(troops) , len(balloons) , len(canons) , len(wizard_towers))
# time.sleep(3)

# print(No_of_canon , No_of_wizard)
# time.sleep(1)

# print(len(buildings))
# time.sleep(5)

c_flag = 0
r_flag = 0 # Rage spell
h_flag = 0 # healing spell

if __name__ == "__main__":
    replay_input = []

    eagle_attack = []

    while(1):

        print(barb_num , archer_num , balloon_num)
        # for wizard1 in wizard_towers:
        #     print(wizard1.get_health())
        
        
    # Check for victory / Level change
        vict_flag = 1
        lost_flag = 1

        for i,building in enumerate(buildings):
            
            if i > (6 + No_of_canon + No_of_wizard - 1):
                break
            if building.getx() != -100:
                vict_flag = 0
        
        if vict_flag == 1:
            if game_level == 3:
                os.system("clear")
                print("Yay , you won the game")
                make_replay(replay_input)

                break
            else :
                game_level += 1
                if type == 'k':
                    make_game_level(game_level , board1 , king1 , buildings , troops , barbs , archers , balloons , canons , wizard_towers , walls , defensive_building)
                else:
                    make_game_level(game_level , board1 , queen1 , buildings , troops , barbs , archers , balloons , canons , wizard_towers , walls , defensive_building)


        if type == 'k' and king1.get_health() > 0 or type == 'q' and queen1.get_health() > 0:
            lost_flag = 0
        for troop1 in troops:
            if troop1.get_health():
                lost_flag = 0
        
        if lost_flag == 1:
            os.system("clear")
            print("You lost :>")
            make_replay(replay_input)
            break

        for bld in buildings:
            if bld.get_health() > 0:
                bld.show(board1._grid)
        
        for ball in balloons:
            if ball.get_health() > 0:
                ball.show_troop(board1._grid)

        


# handling attack of wizard and canons 
        if(time.time() - starttime >= 1.0):
            c_flag = 1-c_flag

            # wizard.attack(balloons)
            
        
            if c_flag==1:

                for canon1 in canons:
                    canon1.set_color(Fore.RED , 6 , board1._grid)

                if type == 'k':

                    for canon1 in canons:
                        canon1.attack(king1 , troops)
                else:
                    for canon1 in canons:
                        canon1.attack(queen1 , troops)

                for wizard1 in wizard_towers:
                    if type == 'k':
                        wizard1.attack(king1 , troops)
                    else :
                        wizard1.attack(queen1 , troops)

            else:
                for canon1 in canons:
                    canon1.set_color(Fore.YELLOW , 6 , board1._grid)

                # if type == 'k':

                #     for canon1 in canons:
                #         canon1.attack(king1 , troops)
                # else:
                #     for canon1 in canons:
                #         canon1.attack(queen1 , troops)
            
            starttime = time.time()


        if r_flag == 1:
            val = input_to(Get(),0.05)
        else:
            val = input_to(Get() , 0.1)
        replay_input.append(val)

        os.system("clear")
        board1.display_grid()

        if type == 'k' and king1.get_health() <= 0:
            print("King is dead :(")
        elif type == 'q' and queen1.get_health() <= 0:
            print("queen is dead :(")
        else :
            health = 0
            if type == 'k':
                health = king1.get_health()
            else :
                health = queen1.get_health()

            num_of_tiles = round(health/100 * 10)
        
            if health > 50:
                for i in range(num_of_tiles):
                    print(Fore.GREEN + "|" + Style.RESET_ALL , end = "")
                print()
                
            elif health > 20:
                for i in range(num_of_tiles):
                    print(Fore.YELLOW + "|" + Style.RESET_ALL , end = "")
                print()
            else:
                for i in range(num_of_tiles):
                    print(Fore.RED + "|" + Style.RESET_ALL , end = "")
                print()


        if(val == 'q' or val == 'Q'):
            break

        elif(val == 'w' or val == 'W'):

            if type == 'k':
                if(king1.get_health()<=0):
                    continue
                board1._grid = king1.move_up(board1._grid)
                king1.direction = "up"
            else :
                if(queen1.get_health()<=0):
                    continue
                board1._grid = queen1.move_up(board1._grid)
                queen1.direction = "up"

        elif(val == 'a' or val == 'A'):
            if type == 'k':
                if(king1.get_health()<=0):
                    continue
                board1._grid = king1.move_left(board1._grid)
                king1.direction = "left"
            else :
                if(queen1.get_health()<=0):
                    continue
                board1._grid = queen1.move_left(board1._grid)
                queen1.direction = "left"

        elif(val == 's' or val == 'S'):
            if type == 'k':
                if(king1.get_health()<=0):
                    continue
                board1._grid = king1.move_down(board1._grid)
                king1.direction = "down"
            else :
                if(queen1.get_health()<=0):
                    continue
                board1._grid = queen1.move_down(board1._grid)
                queen1.direction = "down"

        elif(val == 'd' or val == 'D'):
            if type == 'k':
                if(king1.get_health()<=0):
                    continue
                board1._grid = king1.move_right(board1._grid)
                king1.direction = "right"
            else :
                if(queen1.get_health()<=0):
                    continue
                board1._grid = queen1.move_right(board1._grid)
                queen1.direction = "right"
        
        elif(val == ' '):
            if type == 'k':
                attack1 = attack(king1.getx()  , king1.gety() , 10 , king1.direction , buildings , board1)
                attack1.check_attack_possible()

            else:
                # print("helllo")
                queen1.attack(5 , buildings , board1)
    
                
        
        # 1 , 2 , 3 will spawn the barbarians
        elif(val == '1'):

            if barb_num >= 6:
                continue
            
            barb_num += 1

            troop1 = barb(1 ,5 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK )
            troop1.show_troop(board1._grid)
            barbs.append(troop1)
            troops.append(troop1)

        elif(val == '2'):

            if barb_num >= 6:
                continue
            
            barb_num += 1

            troop1 = barb(1 ,6 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            barbs.append(troop1)
            troops.append(troop1)

        elif(val == '3'):

            if barb_num >= 6:
                continue
            
            barb_num += 1

            troop1 = barb(1 ,7 , 20 , 1 , 2 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            barbs.append(troop1)
            troops.append(troop1)
        
        # 4 , 5, 6 will spawn the archers

        elif(val == '4'):

            if archer_num >= 6:
                continue
            
            archer_num += 1

            troop1 = archer(1 ,5 , 10 , 0.5 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK )
            troop1.show_troop(board1._grid)
            archers.append(troop1)
            troops.append(troop1)

        elif(val == '5'):

            if archer_num >= 6:
                continue
            
            archer_num += 1

            troop1 = archer(1 ,6 , 10 , 0.5 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            archers.append(troop1)
            troops.append(troop1)

        elif(val == '6'):

            if archer_num >= 6:
                continue
            
            archer_num += 1

            troop1 = archer(1 ,7 , 10 , 0.5 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            archers.append(troop1)
            troops.append(troop1)


        # 7 , 8 , 9 will spawn the ballons 
        elif(val == '7'):

            if balloon_num >= 3:
                continue 

            balloon_num += 1

            troop1 = balloon(1 ,5 , 20 , 2 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK )
            troop1.show_troop(board1._grid)
            balloons.append(troop1)
            troops.append(troop1)

        elif(val == '8'):

            if balloon_num >= 3:
                continue 

            balloon_num += 1

            troop1 = balloon(1 ,6 , 20 , 2 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            balloons.append(troop1)
            troops.append(troop1)

        elif(val == '9'):

            if balloon_num >= 3:
                continue 

            balloon_num += 1

            troop1 = balloon(1 ,7 , 20 , 2 , 4 , Fore.LIGHTGREEN_EX + Back.BLACK)
            troop1.show_troop(board1._grid)
            balloons.append(troop1)
            troops.append(troop1)
        
        elif(val == 'r' or val == 'R'):
            r_flag = 1
        elif(val == 'h' or val == 'H'):
            # Increase health of king/queen
            if type == 'k':
                king1.set_health(max(100 , 1.5*king1.get_health()))
            else :
                queen1.set_health(max(100 , 1.5*queen1.get_health()))
                
            #Increase health of all troops
            for troop1 in troops:
                troop1.set_health(max(20 , 1.5*troop1.get_health()))

        # print("hi")
        move_troops(barbs , buildings , board1._grid)
        move_archers(archers , buildings , board1._grid)
        move_balloons(balloons , buildings , board1._grid, defensive_building)
        # print("canon1 : " , buildings[6].get_health() , "canon2 : " , buildings[7].get_health())
            