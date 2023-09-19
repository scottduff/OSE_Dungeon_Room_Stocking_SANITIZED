from random import *
from oseClassicMonsterList import *

def monsterLevelType():
    monsterSpecific = randint(1, 20)
    match monsterSpecific:
        case 1:
            return AcolyteMonster
        case 2:
            return BanditMonster
        case 3:
            return BeetleGiantFireMonster
        case 4:
            return DwarfMonster
        case 5:
            return GnomeMonster
        case 6:
            return GoblinMonster
        case 7:
            return GreenSlimeMonster
        case 8:
            return HalflingMonster
        case 9:
            return KillerBeeMonster
        case 10:
            return KoboldMonster
        case 11:
            return LizardGiantGeckoMonster
        case 12:
            return OrcMonster
        case 13:
            return ShrewGiantMonster
        case 14:
            return SkeletonMonster
        case 15:
            return SnakeSpittingCobraMonster
        case 16:
            return CrabGiantMonster
        case 17:
            return SpriteMonster
        case 18:
            return StirgeMonster
        case 19:
            return TraderMonster
        case 20:
            return WolfNormalMonster
        case _:
            return "Monster Type"
