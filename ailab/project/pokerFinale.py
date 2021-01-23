import random

rank = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
suit = {'s', 'h', 'c', 'd'}

p1 = set()
p2 = set()


def hand():
    p1.clear()
    p2.clear()
    # Counter
    j = 0

    while (True):
        temp = (random.choice(tuple(rank)), random.choice(tuple(suit)))

        if (temp in p1):
            continue
        else:
            p1.add(temp)
            p2.add(temp)
        j += 1

        if (len(p1) == 5):
            break
    # Analysing Hands
    objA = set()
    objB = set()


    for i in p1:
        try:
            objA.add(i[0])
            objB.add(i[1])
        except:
            pass
    #print(objA,"\n", objB)
    #print(len(objA),"\n",len(objB))

    maxA = 0
    minA = 15

    for i in objA:
        try:           
            if('A' in objA):
                maxA = 14
            elif('K' in objA):
                maxA = 13
            elif('Q' in objA):
                maxA = 12
            elif('J' in objA):
                maxA = 11
            else:
                if maxA < int(i):
                    maxA = int(i)
        except:
            pass

    for j in objA:
        try:
            if minA > int(j):
                minA = int(j)
        except:
            pass
    print("*********************************************\n",maxA, minA)

    diff = maxA - minA
    #print(diff)

    # Straight Flush
    if((len(objB) == 1) and (diff == 4)):
        rank1 = "Straight Flush"
        print("Player1's hand is: ", rank1, p1)
        return rank1

    # Four of A Kind
    if(len(objA) == 2):
        rank2 = "Four of A Kind"
        print("Player1's hand is: ", p1)
        return rank2

    # Full House
    if((len(objA) == 2) and (len(objB) >= 3)):
        rank3 = "Full House"
        print("Player1's hand is: ", p1)
        return rank3

    # Flush
    if(len(objB) == 1):
        rank4 = "Flush"
        print("Player1's hand is: ", p1)
        return rank4
    # Straight
    if((len(objA) == 5) and (diff == 4)):
        rank5 = "Straight"
        print("Player1's hand is: ", p1)
        return rank5

    # Three of A Kind
    if (len(objA) == 3):
        rank6 = "Three of A Kind"
        print("layer1's hand is: ", p1)
        return rank6

    # Two Pairs
    if((len(objA) == 3) and (len(objB) >= 2)):
        rank6 = "Two Pairs"
        print("Player1's hand is: ", p1)
        return rank7
    # Pair
    if (len(objA) == 4):
        rank8 = "Pair"
        print("Player1's hand is: ", p1)
        return rank8

    # High Card
    if  (len(objA) == 5):
        rank9 = "High Card"
        print("Player1's hand is: ", p1)
        return rank9

for i in range (0,10):
    print("round: ", 1+i)
    x=hand()
    print(x)

def cardValue():
    value = hand()
