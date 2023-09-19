from random import *

def magicItemType():
    magicItem = ""
    magicSpecific = randint(1, 100)
    if magicSpecific < 11:
        magicItem += magicArmourType()
        return magicItem
    elif magicSpecific < 16 and magicSpecific > 10:
        magicItem += magicMiscType()
        return magicItem
    elif magicSpecific < 41 and magicSpecific > 15:
        magicItem += magicPotionType()
        return magicItem
    elif magicSpecific < 46 and magicSpecific > 40:
        magicItem += magicRingType()
        return magicItem
    elif magicSpecific < 51 and magicSpecific > 45:
        magicItem += magicWandType()
        return magicItem
    elif magicSpecific < 71 and magicSpecific > 50:
        magicItem += magicScrollType()
        return magicItem
    elif magicSpecific < 91 and magicSpecific > 70:
        magicItem += magicSwordType()
        return magicItem
    elif magicSpecific > 90:
        magicItem += magicWeaponType()
        return magicItem
    else:
        return "Magic Item"

def magicArmourType():
    magicArmour = "" 
    armourSpecific =  randint(1, 4)
    match armourSpecific:
        case 1:
            magicArmour += armourType() + " +1"
            return magicArmour
        case 2:
            magicArmour += armourType() + " +1, Shield +1"
            return magicArmour
        case 3:
            magicArmour += armourType() + " AC 9 [10] Cursed"
            return magicArmour
        case 4:
            magicArmour += "Sheild +1"
            return magicArmour
        case _:
            return "Magic Armour"

def armourType():
    armourSpecific =  randint(1, 8)
    match armourSpecific:
        case 1 | 2:
            return "Leather"
        case 3 | 4 | 5 |  6:
            return "Chainmail"
        case 7 | 8:
            return "Platemail"
        case _:
            return "Armour Type"

def magicMiscType():
    miscSpecific = randint(1, 10)
    match miscSpecific:
        case 1:
            return "Bag of Devouring"
        case 2:
            return "Bag of Holding"
        case 3:
            return "Broom of Flying"
        case 4:
            return "Crystal Ball"
        case 5:
            return "Elven Cloak and Boots"
        case 6:
            return "Gaunlets of Ogre Power"
        case 7:
            return "Helm of Alignment Changing"
        case 8:
            return "Helm of Telepathy"
        case 9:
            return "Medallion of ESP 30'"
        case 10:
            return "Rope of Climbing"
        case _:
            return "Misc Magic Item"

def magicPotionType():
    potionSpecific = randint(1, 8)
    match potionSpecific:
        case 1:
            return "Potion of Diminution"
        case 2:
            return "Potion of ESP"
        case 3:
            return "Potion of Gaseous Form"
        case 4:
            return "Potion of Growth"
        case 5:
            return "Potion Healing"
        case 6:
            return "Potion Invisbility"
        case 7:
            return "Potion of Invisbility"
        case 8:
            return "Potion of Levitation"
        case 9:
            return "Potion of Poison"
        case _:
            return "Magic Potion"

def magicRingType():
    ringSpecific = randint(1, 6)
    match ringSpecific:
        case 1:
            return "Ring of Control Animal"
        case 2:
            return "Ring of Fire Resistance"
        case 3:
            return "Ring of Protection +1"
        case 4:
            return "Ring of Water Walking"
        case 5:
            return "Ring of Water Walking"
        case 6:
            return "Ring of Weakness"
        case _:
            return "Magic Ring"

def magicWandType():
    wandSpecific = randint(1, 6)
    match wandSpecific:
        case 1:
            return "Rod of Cancellation"
        case 2:
            return "Staff of Healing"
        case 3:
            return "Staff of Snakes"
        case 4:
            return "Wand of Enemy Detection"
        case 5:
            return "Wand of Magic Detection"
        case 6:
            return "Wand of Paralysation"
        case _:
            return "Magic Wand"

def magicScrollType():
    scrollSpecific = randint(1, 8)
    match scrollSpecific:
        case 1:
            return "Scroll (1) spell"
        case 2:
            return "Scroll (2) spells"
        case 3:
            return "Scroll (3) spells"
        case 4:
            return "Cursed Scroll"
        case 5:
            return "Scroll of Protection from Lycanthropes"
        case 6:
            return "Scroll of Protection from Undead"
        case 7:
            return "Treasure Map I: Location of 1 Magic Item"
        case 8:
            return "Treasure Map VIII: Hoard of 5d6 x 1000 gp"
        case _:
            return "Magic Scroll"

def magicSwordType():
    magicSword = "" 
    swordSpecific =  randint(1, 8)
    match swordSpecific:
        case 1:
            magicSword += swordType() + " -1, Cursed"
            return magicSword
        case 2:
            magicSword += swordType() + " +1"
            return magicSword
        case 3:
            magicSword += swordType() + " +1, +2 vs Lycanthropes"
            return magicSword
        case 4:
            magicSword += swordType() + " +1, +2 vs Spell Users"
            return magicSword
        case 5:
            magicSword += swordType() + " +1, +2 vs Dragons"
            return magicSword
        case 6:
            magicSword += swordType() + " +1, +2 vs Undead"
            return magicSword
        case 7:
            magicSword += swordType() + " +1, Light"
            return magicSword
        case 8:
            magicSword += swordType() + " +2"
            return magicSword
        case _:
            return "Magic Sword"

def swordType():
    magicSword =  randint(1, 6)
    match magicSword:
        case 1 | 2 | 3:
            return "Sword"
        case 4 | 5:
            return "Short Sword"
        case 6:
            return "Two-handed Sword"
        case _:
            return "Magic Sword"

def magicWeaponType():
    magicWeapon = "" 
    weaponSpecific =  randint(1, 4)
    match weaponSpecific:
        case 1:
            magicWeapon += "Arrows +1" + str((randint(1, 6) + randint(1, 6))) + " +1"
            return magicWeapon
        case 2:
            magicWeapon += axeType() + " +1"
            return magicWeapon
        case 3:
            magicWeapon += "Dagger +1"
            return magicWeapon
        case 4:
            magicWeapon += "Mace +1"
            return magicWeapon
        case _:
            return "Magic Weapon"

def axeType():
    magicAxe =  randint(1, 6)
    match magicAxe:
        case 1 | 2 | 3 | 4 | 5:
            return "Hand axe"
        case 6:
            return "Battle axe"
        case _:
            return "Magic Axe"
