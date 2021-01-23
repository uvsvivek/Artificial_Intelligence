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

    print(objA,"\n", objB)
    print(len(objA),"\n",len(objB))

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
        return rank1, 0, 1

    # Four of A Kind
    if(len(objA) == 2):
        rank2 = "Four of A Kind"
        print("Player1's hand is: ", p1)
        return rank2, 0, 1

    # Full House
    if((len(objA) == 2) and (len(objB) >= 3)):
        rank3 = "Full House"
        print("Player1's hand is: ", p1)
        return rank3, 0, 1

    # Flush
    if(len(objB) == 1):
        rank4 = "Flush"
        print("Player1's hand is: ", p1)
        return rank4, 0, 1
    # Straight
    if((len(objA) == 5) and (diff == 4)):
        rank5 = "Straight"
        print("Player1's hand is: ", p1)
        return rank5, 0, 2

    # Three of A Kind
    if (len(objA) == 3):
        rank6 = "Three of A Kind"
        print("layer1's hand is: ", p1)
        return rank6, 0, 1

    # Two Pairs
    if((len(objA) == 3) and (len(objB) >= 2)):
        rank6 = "Two Pairs"
        print("Player1's hand is: ", p1)
        return rank7, 0, 2
    # Pair
    if (len(objA) == 4):
        rank8 = "Pair"
        print("Player1's hand is: ", p1)
        return rank8, 0, 2

    # High Card
    if  (len(objA) == 5):
        rank9 = "High Card"
        print("Player1's hand is: ", p1)
        if ('A' in objA or 'K' in objA or 'Q' in objA or 'J' in objA):
            return rank9, 0, 2
        else:
            return rank9, 0, 0

for i in range (0,2):
    print("round: ", 1+i)
    handType, openGame, bettingType = hand()
    print("Hand Type: ", handType,"\nOpen Game Type: ",openGame,"\nBetting Type: ",bettingType)

def open():
    handType, openGame, bettingType = hand()
    if(openGame == 0):
        return ClientBase.BettingAnswer.ACTION_CHECK
    elif(openGame == 1):
        return ClientBase.BettingAnswer.ACTION_ALLIN
    else:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN, (random.randint(0,
                                                                         10) + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen

def raiseCall():
    handType, openGame, bettingType = hand()
    if(bettingType == 0):
        return ClientBase.BettingAnswer.ACTION_FOLD
    elif(bettingType == 1):
        return ClientBase.BettingAnswer.ACTION_ALLIN
    elif(bettingType == 2):
        return ClientBase.BettingAnswer.ACTION_CALL
    else:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE, (random.randint(0,
                                                                          10) + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo
