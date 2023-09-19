from random import *

class DungeonRoomGenerator():

    def __init__(self):

        rooms = [
            "Empty", 
            "Monster", 
            "Special", 
            "Trap"
        ]

        self.room = choice(rooms)
        self.level = floorLevel

    def getRooms(self):
        return f"Room Count {self.room}"
    

try:
    roomCount = int(input("How many dungeon rooms to generate? Enter to exit.\n"))
    print(">")
    floorLevel = int(input("What dungeon level are the rooms on? Enter to exit.\n"))
    print(">")

except:
    raise SystemExit


file = open("dungeonRooms.txt", "a")


for x in range(roomCount):
    DungeonRoom = DungeonRoomGenerator()
    print(DungeonRoom.getRooms() + '\n')
    file.write(DungeonRoom.getRooms() + '\n\n')





file.close()
input('Dungeon rooms exported to "dungeonRooms.txt". Press Enter to exit.')




