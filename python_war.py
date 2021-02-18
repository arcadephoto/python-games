import random


class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name





class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class In_play:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

class Game:
    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.player1 = Player(self.hand1, input("Player 1 Name:  "))
        self.player2 = Player(self.hand2, input("Player 2 Name:  "))
        self.deck = Deck()
        self.count = 0

    def card_deal(self):
        for i in range(1, 27):
            self.hand1.append(self.deck.cards.pop())
            self.hand2.append(self.deck.cards.pop())

    def shuffle_hand(self):
        print("Shuffling both hands!")
        random.shuffle(self.player1.hand)
        random.shuffle(self.player2.hand)

class Deck:
    def __init__(self):
        self.cards = []
        self.gen_deck()

    def gen_suit(self, suit):
        for i in range(1, 14):
            card = Card(i, suit)
            self.cards.append(card)

    def gen_deck(self):
        self.gen_suit("hearts")
        self.gen_suit("diamonds")
        self.gen_suit("clubs")
        self.gen_suit("spades")
        random.shuffle(self.cards)



def compare_cards():
    at_war = False
    inplay = In_play(game.player1.hand.pop(), game.player2.hand.pop())
    print(game.player1.name, "plays", inplay.card1, game.player2.name, "plays", inplay.card2)
    if inplay.card1.value > inplay.card2.value:
        print(game.player1.name," wins.")
        game.player1.hand.insert(0, inplay.card1)
        game.player1.hand.insert(0, inplay.card2)
    if inplay.card1.value < inplay.card2.value:
        print(game.player2.name, "wins.")
        game.player2.hand.insert(0, inplay.card1)
        game.player2.hand.insert(0, inplay.card2)
    if inplay.card1.value == inplay.card2.value:
        print("WAR!")
        at_war = True
        game.player1.hand.append(inplay.card1)
        game.player2.hand.append(inplay.card2)
        do_war()
    if at_war == False:
        game.count = game.count +1
        if game.count == 26:
            game.shuffle_hand()
            game.count = 0
        end_hand()
#         play_again()
        compare_cards()


def do_war():
    if len(game.player1.hand) < 4:
        print(game.player1.name, "doesn't have enough cards for War.", game.player2.name, "wins!")
        return
    if len(game.player2.hand) < 4:
        print(game.player2.name, "doesn't have enough cards for War.", game.player1.name, "wins!")
        return
    for i in range(1, 5):
        warchest.insert(0, game.player1.hand.pop())
        warchest.insert(0, game.player2.hand.pop())
    c1 = game.player1.hand.pop()
    c2 = game.player2.hand.pop()
    warchest.insert(0, c1)
    warchest.insert(0, c2)
#     warchest.insert(0, inplay.warcards[1])
#     warchest.insert(0, inplay.warcards[0])
#     print("C1 and C2", c1, c2)
#     print("WARCHEST", warchest)
#     print("Player 1 plays", c1, ". Player 2 plays", c2)
    if c1.value > c2.value:
        at_war = False
        print(game.player1.name, " wins!")
        while len(warchest) > 0:
            game.player1.hand.insert(0, warchest.pop())
    if c2.value > c1.value:
        at_war = False
        print(game.player2.name, " wins!")
        while len(warchest) > 0:
            game.player2.hand.insert(0, warchest.pop())
    if c1.value == c2.value:
        print("The same value. Alas, the war continues.")
        at_war = True
        do_war()
    if len(game.player1.hand) < 1:
        print(game.player2.name, "has won!")
        return
    if len(game.player2.hand) < 1:
        print(game.player1.name, "has won!")
        return
    if at_war == False:
        end_hand()
        play_again()

#     print("WARCHEST AFTER", warchest)
#     print(game.player1.hand)
#     print(game.player2.hand)

def end_hand():
    print(game.player1.name, "has", len(game.player1.hand), "cards.")
    print(game.player2.name, "has", len(game.player2.hand), "cards.")

def play_again():
    print("Play again?")
    if input() == "y":
        compare_cards()

warchest = []
game=Game()
game.card_deal()
compare_cards()
