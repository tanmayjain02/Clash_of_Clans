# from tkinter.tix import Balloon
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
# from troop import *

SCR_HEIGHT = 30
SCR_WIDTH = 60

barb_num = 0
archer_num = 0
balloon_num = 0 

game_level = 1

defensive_buildings = []

type = 'k'

No_of_canon = 2
No_of_wizard = 2