__author__ = 'fyt'

import socket
import random
import ClientBase
import collections

# IP address and port
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
count = 0
# Agent
POKER_CLIENT_NAME = 'Moni'
CURRENT_HAND = []
hand = []
cardstring = ""
card_list1 = []
suits = []
numbers = []
throw_cardstring = ""
throw_card_list1 = []
throw_suits = []
throw_numbers = []
rank = "Nothing"
rank1 = "Straight-Flush"
rank2 = "Four-of-a-kind"
rank3 = "Full-House"
rank4 = "Flush"
rank5 = "Straight"
rank6 = "Three-of-a-kind"
rank7 = "Two-Pair"
rank8 = "One-Pair"
rank9 = "High Card"


class pokerGames(object):
    def __init__(self):
        self.PlayerName = POKER_CLIENT_NAME
        self.Chips = 0
        self.CurrentHand = 0
        self.Ante = 0
        self.playersCurrentBet = 0


'''
* Gets the name of the player.
* @return  The name of the player as a single word without space. <code>null</code> is not a valid answer.
'''


def queryPlayerName(_name):
    if _name is None:
        _name = POKER_CLIENT_NAME
    return _name

def infoCardsInHand(_hand):
    global hand
    hand= _hand[-5:]
    strength = cardstrength(hand)
    print(strength)


'''
* Modify queryOpenAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what open
* action to choose.
* @param minimumPotAfterOpen   the total minimum amount of chips to put into the pot if the answer action is
*                              {@link BettingAnswer#ACTION_OPEN}.
* @param playersCurrentBet     the amount of chips the player has already put into the pot (dure to the forced bet).
* @param playersRemainingChips the number of chips the player has not yet put into the pot.
* @return                      An answer to the open query. The answer action must be one of
*                              {@link BettingAnswer#ACTION_OPEN}, {@link BettingAnswer#ACTION_ALLIN} or
*                              {@link BettingAnswer#ACTION_CHECK }. If the action is open, the answers
*                              amount of chips in the anser must be between <code>minimumPotAfterOpen</code>
*                              and the players total amount of chips (the amount of chips alrady put into
*                              pot plus the remaining amount of chips).
'''


def queryOpenAction(_minimumPotAfterOpen, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose an opening action.")

    x = open()
    if(x==0):
        return ClientBase.BettingAnswer.ACTION_CHECK
    elif(x==1):
        return ClientBase.BettingAnswer.ACTION_ALLIN
    else:
        if _playersCurrentBet + _playersRemainingChips > _minimumPotAfterOpen:
            return ClientBase.BettingAnswer.ACTION_OPEN, (random.randint(0,
                                                                         10) + _minimumPotAfterOpen) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumPotAfterOpen else _minimumPotAfterOpen


'''
* Modify queryCallRaiseAction() and add your strategy here
* Called during the betting phases of the game when the player needs to decide what call/raise
* action to choose.
* @param maximumBet                the maximum number of chips one player has already put into the pot.
* @param minimumAmountToRaiseTo    the minimum amount of chips to bet if the returned answer is {@link BettingAnswer#ACTION_RAISE}.
* @param playersCurrentBet         the number of chips the player has already put into the pot.
* @param playersRemainingChips     the number of chips the player has not yet put into the pot.
* @return                          An answer to the call or raise query. The answer action must be one of
*                                  {@link BettingAnswer#ACTION_FOLD}, {@link BettingAnswer#ACTION_CALL},
*                                  {@link BettingAnswer#ACTION_RAISE} or {@link BettingAnswer#ACTION_ALLIN }.
*                                  If the players number of remaining chips is less than the maximum bet and
*                                  the players current bet, the call action is not available. If the players
*                                  number of remaining chips plus the players current bet is less than the minimum
*                                  amount of chips to raise to, the raise action is not available. If the action
*                                  is raise, the answers amount of chips is the total amount of chips the player
*                                  puts into the pot and must be between <code>minimumAmountToRaiseTo</code> and
*                                  <code>playersCurrentBet+playersRemainingChips</code>.
'''


def queryCallRaiseAction(_maximumBet, _minimumAmountToRaiseTo, _playersCurrentBet, _playersRemainingChips):
    print("Player requested to choose a call/raise action.")

    x = callplay()
    if (x == 0):
        return ClientBase.BettingAnswer.ACTION_FOLD
    elif(x == 1):
        return ClientBase.BettingAnswer.ACTION_ALLIN
    elif(x==2):
        return ClientBase.BettingAnswer.ACTION_CALL
    else:
        if _playersCurrentBet + _playersRemainingChips > _minimumAmountToRaiseTo:
            return ClientBase.BettingAnswer.ACTION_RAISE, (random.randint(0,
                                                                          10) + _minimumAmountToRaiseTo) if _playersCurrentBet + _playersRemainingChips + 10 > _minimumAmountToRaiseTo else _minimumAmountToRaiseTo



'''
* Modify queryCardsToThrow() and add your strategy to throw cards
* Called during the draw phase of the game when the player is offered to throw away some
* (possibly all) of the cards on hand in exchange for new.
* @return  An array of the cards on hand that should be thrown away in exchange for new,
*          or <code>null</code> or an empty array to keep all cards.
* @see     #infoCardsInHand(ca.ualberta.cs.poker.Hand)
'''


def queryCardsToThrow(_hand):
    print("Requested information about what cards to throw")
    print(_hand)
    throw_cardstring = ''.join(_hand[-5:])
    throw_card_list1 = list(throw_cardstring)
    throw_suits = throw_card_list1[1::2]
    throw_numbers = throw_card_list1[0::2]
    strength = cardstrength(hand)
    throw_card_index = 0
    if strength == rank1:
        throw_card_index = throw_numbers.index("K")
        if throw_card_index == 0:
            return _hand[1]
        elif throw_card_index > 0:
            return _hand[throw_card_index - 1]

    elif strength == rank2:
        if throw_numbers.count(throw_numbers[0]) != 4:
            return _hand[0] + ' '
        elif throw_numbers.count(throw_numbers[1]) != 4:
            return _hand[1] + ' '
        elif throw_numbers.count(throw_numbers[2]) != 4:
            return _hand[2] + ' '
        elif throw_numbers.count(throw_numbers[3]) != 4:
            return _hand[3] + ' '
        elif throw_numbers.count(throw_numbers[4]) != 4:
            return _hand[4] + ' '

    elif strength == rank3:
        throw_card_index = throw_numbers.index("K")
        return _hand[throw_card_index] + ' '
    elif strength == rank4:
        return _hand[0]
    elif strength == rank5:
        return _hand[0]
    elif strength == rank6:

        if throw_numbers.count(throw_numbers[0]) != 3:
            return _hand[0]

        if throw_numbers.count(throw_numbers[1]) != 3:
            return _hand[1]

        if throw_numbers.count(throw_numbers[2]) != 3:
            return _hand[2]

        if throw_numbers.count(throw_numbers[3]) != 3:
            return _hand[3]

        if throw_numbers.count(throw_numbers[4]) != 3:
            return _hand[4]


    elif strength == rank7:
        if throw_numbers.count(throw_numbers[0]) != 2:
            return _hand[0] + ' '
        elif throw_numbers.count(throw_numbers[1]) != 2:
            return _hand[1] + ' '
        elif throw_numbers.count(throw_numbers[2]) != 2:
            return _hand[2] + ' '
        elif throw_numbers.count(throw_numbers[3]) != 2:
            return _hand[3] + ' '
        elif throw_numbers.count(throw_numbers[4]) != 2:
            return _hand[4] + ' '

    elif strength == rank8:

        if throw_numbers.count(throw_numbers[0]) != 2:
            return _hand[0]

        if throw_numbers.count(throw_numbers[1]) != 2:
            return _hand[1]

        if throw_numbers.count(throw_numbers[2]) != 2:
            return _hand[2]

        if throw_numbers.count(throw_numbers[3]) != 2:
            return _hand[3]

        if throw_numbers.count(throw_numbers[4]) != 2:
            return _hand[4]


    elif strength == rank9:
        index1 = throw_numbers.index("K")
        if index1 == 0:
            return _hand[index1+1]
        else:
            return _hand[index1-1]


# InfoFunction:

'''
* Called when a new round begins.
* @param round the round number (increased for each new round).
'''


def infoNewRound(_round):
    # _nrTimeRaised = 0
    print('Starting Round: ' + _round)


'''
* Called when the poker server informs that the game is completed.
'''


def infoGameOver():
    print('The game is over.')


'''
* Called when the server informs the players how many chips a player has.
* @param playerName    the name of a player.
* @param chips         the amount of chips the player has.
'''


def infoPlayerChips(_playerName, _chips):
    print('The player ' + _playerName + ' has ' + _chips + 'chips')


'''
* Called when the ante has changed.
* @param ante  the new value of the ante.
'''


def infoAnteChanged(_ante):
    print('The ante is: ' + _ante)


'''
* Called when a player had to do a forced bet (putting the ante in the pot).
* @param playerName    the name of the player forced to do the bet.
* @param forcedBet     the number of chips forced to bet.
'''


def infoForcedBet(_playerName, _forcedBet):
    print("Player " + _playerName + " made a forced bet of " + _forcedBet + " chips.")


'''
* Called when a player opens a betting round.
* @param playerName        the name of the player that opens.
* @param openBet           the amount of chips the player has put into the pot.
'''


def infoPlayerOpen(_playerName, _openBet):
    print("Player " + _playerName + " opened, has put " + _openBet + " chips into the pot.")


'''
* Called when a player checks.
* @param playerName        the name of the player that checks.
'''


def infoPlayerCheck(_playerName):
    print("Player " + _playerName + " checked.")


'''
* Called when a player raises.
* @param playerName        the name of the player that raises.
* @param amountRaisedTo    the amount of chips the player raised to.
'''


def infoPlayerRise(_playerName, _amountRaisedTo):
    print("Player " + _playerName + " raised to " + _amountRaisedTo + " chips.")


'''
* Called when a player calls.
* @param playerName        the name of the player that calls.
'''


def infoPlayerCall(_playerName):
    print("Player " + _playerName + " called.")


'''
* Called when a player folds.
* @param playerName        the name of the player that folds.
'''


def infoPlayerFold(_playerName):
    print("Player " + _playerName + " folded.")


'''
* Called when a player goes all-in.
* @param playerName        the name of the player that goes all-in.
* @param allInChipCount    the amount of chips the player has in the pot and goes all-in with.
'''


def infoPlayerAllIn(_playerName, _allInChipCount):
    print("Player " + _playerName + " goes all-in with a pot of " + _allInChipCount + " chips.")


'''
* Called when a player has exchanged (thrown away and drawn new) cards.
* @param playerName        the name of the player that has exchanged cards.
* @param cardCount         the number of cards exchanged.
'''


def infoPlayerDraw(_playerName, _cardCount):
    print("Player " + _playerName + " exchanged " + _cardCount + " cards.")


'''
* Called during the showdown when a player shows his hand.
* @param playerName        the name of the player whose hand is shown.
* @param hand              the players hand.
'''


def infoPlayerHand(_playerName, _hand):
    print("Player " + _playerName + " hand " + str(_hand))


'''
* Called during the showdown when a players undisputed win is reported.
* @param playerName    the name of the player whose undisputed win is anounced.
* @param winAmount     the amount of chips the player won.
'''


def infoRoundUndisputedWin(_playerName, _winAmount):
    print("Player " + _playerName + " won " + _winAmount + " chips undisputed.")


'''
* Called during the showdown when a players win is reported. If a player does not win anything,
* this method is not called.
* @param playerName    the name of the player whose win is anounced.
* @param winAmount     the amount of chips the player won.
'''


def infoRoundResult(_playerName, _winAmount):
    print("Player " + _playerName + " won " + _winAmount + " chips.")


def cardstrength(hand):
    #print(hand)
    cardstring = ''.join(hand)
    card_list1 = list(cardstring)
    suits = card_list1[1::2]
    numbers = card_list1[0::2]
    for i, num in enumerate(numbers):
        if num == "A":
            numbers[i] = 14
        elif num == "K":
            numbers[i] = 13
        elif num == "Q":
            numbers[i] = 12
        elif num == "J":
            numbers[i] = 11
        elif num == "T":
            numbers[i] = 10

    # print(suits)
    print(numbers)
    num_dict = collections.defaultdict(int)
    suit_dict = collections.defaultdict(int)
    for i in numbers:
        num_dict[i] += 1
    for j in suits:
        suit_dict[j] += 1
    # num_dict = {i:numbers.count(i) for i in numbers}
    print(max(numbers))
    print(min(numbers))

           # 4-of-a-kind
    if len(num_dict) == 2:
        if 4 in num_dict.values():
            rank = rank2
            return rank
            print(rank)
        # Full house

    elif len(num_dict) == 2:
        if 3 in num_dict.values():
            for my_card in numbers:
                if my_card == "K":
                    count = count + 1
            if count == 2:
                rank = rank3
                return rank
                print(rank)

        # flush

    elif len(suit_dict) == 1:
        if 5 in suit_dict.values():
            rank = rank4
            return rank
            print(rank)

        # straight

    elif len(num_dict) == 5:

        max_val = (max([numbers.index(x) for x in num_dict.keys()]))
        min_val = (min([numbers.index(x) for x in num_dict.keys()]))
        # print(max_val,min_val)
        if int(max_val) - int(min_val) == 4:
            rank = rank5
            return rank
            print(rank)
            # Case of Ace
            # ace_set = set(("A", "2", "3", "4", "5"))
            # if not set(num_dict.keys()).difference(ace_set):
            #  rank = rank5

        # 3-of-a-kind
    elif len(num_dict) == 3:
        if 3 in num_dict.values():
            rank = rank6
            return rank
            print(rank)

            # 2 Pair
    elif len(num_dict) == 3:
        if 2 in num_dict.values():
            rank = rank7
            return rank
            print(rank)

            # 1 Pair
    elif len(num_dict) == 2:
        rank = rank8
        return rank
        print(rank)


    elif len(num_dict) == 3:
        for my_card in numbers:
            if my_card == "K":
                rank = rank9
                return rank
                print(rank)



def open():
    handstring = ''.join(hand)
    handlist =  list(handstring)
    count1 = 0
    strength = cardstrength(hand)
    if strength == rank1:
        return 0
    else:
        if strength ==rank2:
            if count1 == 0:
                count1 = count1 + 1
                return 0
            else:
                return 1

        elif(strength == rank6):
            return 0

        elif(strength == rank7):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1
        if(strength == rank8):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1
        elif(strength == rank4):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1

        elif(strength == rank3):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1
        elif(strength ==rank9):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1

        if(strength == rank5):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1

        if(strength == rank4):
            if count1 == 0:
                count1 = count1+1
                return 0
            else:
                return 1




def callplay():
    handstring = ''.join(hand)
    handlist = list(handstring)
    count1 = 0
    strength = cardstrength(hand)
    if (strength == rank1):
        return 1
    else:

        if (strength == rank2):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1
        elif (strength == rank6):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1
        elif (strength == rank7):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1

        if (strength == rank8):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1

        elif (strength == rank4):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1
        elif (strength == rank3):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1
        elif (strength == rank9):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1

        if (strength == rank5):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1

        if (strength == rank4):
            if count1 == 0:
                count1 = count1+1
                return 2
            else:
                return 1






