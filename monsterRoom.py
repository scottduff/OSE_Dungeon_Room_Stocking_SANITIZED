from random import *
from gemTreasure import *
from jewelleryTreasure import *
from magicTreasure import *
from oseClassicMonsterList import *
from oseClassicDungeonEncounters import *

def monsterRoomGen():
    coinPieces = ""
    gemPieces = ""
    jewelleryPieces = ""
    magicItem = ""
    monsterChoice = ""

    monsterRoomBlock = '''
        Monster Room


        Monster:    {moChoice}

        Treasure:   {coPieces}
                                    
        Gems:       {gePieces}
                     
        Jewellery:  {jePieces}
                    
        Magic Item: {maItems}

        '''

    monsterSpecific = monsterLevelType()
    for key, value in monsterSpecific[0].items():
        monsterChoice += (str(key) + ": " + str(value) + "\n" + "                    ")

    if (randint(1, 1)) == 1:
        coinPieces += (str(randint(1, 6) * 100) + " sp" + "\n" + "                    ")
        if (randint(1, 100) < 99):
            coinPieces += (str(randint(1, 6) * 10) + " gp" + "\n")
        if (randint(1, 100) < 99):
            for i in range(1, (randint(1, 7))):
                gemPieces += (str(gemType())) + ": " + (str(gemValue()) + "\n" + "                    ")
        if (randint(1, 100) < 99):
            for i in range(1, (randint(1, 7))):
                jewelleryPieces += (str(jewelleryType())) + ": " + (str(jewelleryValue()) + "\n" + "                    ")
        if (randint(1, 100) < 99):
            magicItem += magicItemType()
    
    print(monsterRoomBlock.format(coPieces = coinPieces, gePieces = gemPieces, jePieces = jewelleryPieces, maItems = magicItem, moChoice = monsterChoice))

    return

# monsterRoomGen()
