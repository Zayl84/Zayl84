from random import *
print("1=yes and 0=no, if fight and stats menu selected, fight goes first")
level = 1
HpHeroIn = 20
atk = 10
xp = 0
turn = 1
def menu (fight, stats, level, HpHeroIn, atk, xp, turn):
    prize = 0
    if fight == 1:
        hp = randint(0, int(level/2)) *level + randint(0, level) * randint (1, rep+1) + level
        hpIn = hp
        HpHero = HpHeroIn
        turn = turn + 1
        while hp > 0 :
            HpHero = HpHero -  randint(1, hp)
            hp = int(hp - atk)
            if HpHero <= 0:
                print("You lose")
                return level, HpHeroIn, atk, xp, turn
        xp = xp + int(uniform(1, 300)) + int(uniform(1, 50))
        while xp > 100:
            xp = xp - 100
            level = level + 1
            HpHeroIn = int(HpHeroIn + randint(1, level*2))
            atk = int(atk + randint(1, level*2))
        print("You won and beat a monster with", hpIn, "hp and", HpHero, "hp left")
    if stats == 1:
        print("You are level", level, ", you have ", HpHeroIn, " hp, ", atk, " atk and ", xp, " xp points. You are turn", turn, ".")
    prize = randint(0, 1000)
    if prize == 1:
        print("\033[1;36;40m Thx for playing, you're a champion")
        HpHeroIn = HpHeroIn + level**4
        atk = atk + level**4
        print("You have bonus stats ! You are level", level, ", you have ", HpHeroIn, " hp and ", atk, " atk and ", xp, " xp points.")
        print("menu(1, 1, ", level, ", ", HpHeroIn, ", ", atk, ", ", xp, ")")
        print("\033[0;37;40m ")
    elif prize <= 10:
        print("\033[1;33;40m Thx for playing, you're an elite")
        HpHeroIn = HpHeroIn + level**2
        atk = atk + level**2
        print("You have bonus stats ! You are level", level, ", you have ", HpHeroIn, " hp and ", atk, " atk and ", xp, " xp points.")
        print("menu(1, 1, ", level, ", ", HpHeroIn, ", ", atk, ", ", xp, ")")
        print("\033[0;37;40m ")
    else :
        print("\033[0;37;40m Thx for playing")
    return level, HpHeroIn, atk, xp, turn
fight = int(input("Do you want to fight ?"))
stats = int(input("Do you want to see your stats ?"))
rep = int(input("How many fights would you like ?"))
for i in range(rep):
    changes = menu(fight, stats, level, HpHeroIn, atk, xp, turn)
    list(changes)
    level = int(changes[0])
    HpHeroIn = int(changes[1])
    atk = int(changes[2])
    xp = int(changes[3])
    turn = int(changes[4])
