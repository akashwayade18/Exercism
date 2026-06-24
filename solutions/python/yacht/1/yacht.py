# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'

# BRUTE FORCE
def score(dice, category):
    if category == ONES:
        return 1 * dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    dice.sort()
    if category == LITTLE_STRAIGHT:
        if  dice == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if dice == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    elif category == FULL_HOUSE:
        if ((all(dice[0] == i for i in dice[0: 3]) and all(dice[3] == i for i in dice[3: 5])) or (all(dice[0] == i for i in dice[0: 2]) and all(dice[2] == i for i in dice[2: 5]))) and dice.count(dice[0]) != 5:
            return sum(i for i in dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if all(dice[0] == i for i in dice[0: 4]):
            return sum(i for i in dice[0: 4])
        elif all(dice[1] == i for i in dice[1: 5]):
            return sum(i for i in dice[1: 5])
        else:
            return 0
    elif category == CHOICE:
        return sum(i for i in dice)
    elif category == YACHT:
        if dice.count(dice[0]) == 5:
            return 50
        else:
            return 0
    else:
        return 0