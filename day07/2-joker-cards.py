# https://www.reddit.com/r/adventofcode/comments/18cnzbm/comment/kcndip1/?utm_source=share&utm_medium=web2x&context=3

import time

with open("input/puzzle.txt", "r") as file:
    data = file.readlines()

start = time.time()
data = [x.replace("\n", "") for x in data]
hands = [x.split(" ") for x in data]
valRanking  = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", 
                "Q", "K", "A"]


def getValues(hand):
    hand, name = hand[0], hand[1]
    counts = []
    jokerCount = hand.count("J")
    for uniqLetter in set(hand):
        if uniqLetter != "J":
            counts.append(hand.count(uniqLetter))

    if jokerCount >= 4 or 5 in counts or 5-jokerCount in counts:
        return 6
    if 4 in counts or 4-jokerCount in counts:
        return 5
    if len(counts) == 2:
        return 4
    if 3 - jokerCount in counts:
        return 3
    if counts.count(2) + jokerCount == 2:
        return 2
    if 2 - jokerCount in counts:
        return 1
    return 0    

def getSecondaryRank(card):
    hand = card[0]
    secondaryVals = 0
    for i in range(len(hand)):
        secondaryVals += (valRanking.index(hand[i]) + 1)*14**(len(hand)-i)
    return secondaryVals

valedHands = [[hand[0], hand[1], getValues(hand), getSecondaryRank(hand)] for hand in hands]

valedHands.sort(key=lambda x: (x[2] ,x[3]))

totalWinnings = 0
for i in range(len(valedHands)):
    totalWinnings += (i+1)*int(valedHands[i][1])
print(time.time()-start)
print(totalWinnings)