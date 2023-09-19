from random import *

def jewelleryValue():
    return str((randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100) + " gp"

def jewelleryType():
    jewellerySpecific = (randint(1, 6))
    match jewellerySpecific:
        case 1:
            return "Necklace"
        case 2:
            return "Earrings"
        case 3:
            return "Ring    "
        case 4:
            return "Crown   "
        case 5:
            return "Tiara   "
        case 6:
            return "Chalice "
        case _:          
            return "Jewellery Type"


