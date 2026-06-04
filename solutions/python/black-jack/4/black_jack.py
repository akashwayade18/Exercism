"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    value = None
    if card == 'A':
        value = 1
    elif card in {'J', 'K', 'Q'}:
        value = 10
    else :
        value = int(card)
    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    value_card1 = value_of_card(card_one)
    value_card2 = value_of_card(card_two)
    ans = None

    if value_card1 > value_card2:
        ans = str(card_one)
    elif value_card2 > value_card1:
        ans = str(card_two)
    else :
        ans = card_one, card_two
    return ans


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    value_card1 = value_of_card(card_one)
    value_card2 = value_of_card(card_two)
    ans = None

    if card_one == 'A' or card_two == 'A':
        ans = 1
    elif value_card1 + value_card2 + 11 <= 21:
        ans = 11
    else:
        ans = 1
    return ans


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    value_card1 = value_of_card(card_one)
    value_card2 = value_of_card(card_two)
    ans = None
    allowed_cards = ['A', 'J', 'K', 'Q', '10']
    if value_card1 + value_card2 == 21:
        ans = True
    elif card_one == 'A' and card_two == 'A':
        ans = False
    elif (card_one in allowed_cards and card_two in allowed_cards) and (card_one == 'A' or card_two == 'A'):
        ans = True
    else: 
        ans = False
    return ans
    


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    value_card1 = value_of_card(card_one)
    value_card2 = value_of_card(card_two)
    ans = None

    if value_card1 == value_card2:
        ans = True
    else: 
        ans = False
    return ans


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    value_card1 = value_of_card(card_one)
    value_card2 = value_of_card(card_two)
    ans = None

    if 9 <= value_card1 + value_card2 <= 11:
        ans = True
    else:
        ans = False
    return ans