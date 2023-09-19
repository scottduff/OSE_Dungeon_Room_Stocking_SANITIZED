from random import *

def gemValue():
    gemGoldPieces = (randint(1, 20))
    match gemGoldPieces:
        case 1 | 2 | 3 | 4:
            return "10 gp"
        case 5 | 6 | 7 | 8 | 9:
            return "50 gp"
        case 10 | 11 | 12 | 13 | 14 | 15:
            return "100 gp"
        case 16 | 17 | 18 | 19:
            return "500 gp"
        case 20:
            return "1000 gp"
        case _:
         return "Gem Value"

def gemType():
    gemSpecific = (randint(1, 10))
    match gemSpecific:
        case 1:
            return "Amber   "
        case 2:
            return "Amethyst"
        case 3:
            return "Garnet  "
        case 4:
            return "Pearl   "
        case 5:
            return "Opal    "
        case 6:
            return "Topaz   "
        case 7:
            return "Ruby    "
        case 8:
            return "Emerald "
        case 9:
            return "Sapphire"
        case 10:
            return "Diamond "
        case _:
            return "Gem Type"


