# Code to import from Excel
# from pandas import *
# excel_df = read_excel('book1.xlsx')
# excelVar = excel_df.to_dict('records')
# print(excelVar)

from random import *
from emptyRoom import *
from monsterRoom import *
from specialRoom import *
from trapRoom import *
from gemTreasure import *

def dungeonRoomContents():
    roomType = randint(1, 6)
    match roomType:
        case 1 | 2:
            return emptyRoomGen()
        case 3 | 4:
            return monsterRoomGen()
        case 5:
            return specialRoomGen()
        case 6:
            return trapRoomGen()
        case _:
            return





dungeonRoomContents()



# from pandas import *
# excel_df = read_excel('book1.xlsx')
# excelVar = excel_df.to_dict('records')
# print(excelVar)






