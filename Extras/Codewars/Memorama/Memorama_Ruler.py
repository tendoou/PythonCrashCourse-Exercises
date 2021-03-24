from Memorama import Card
import random
import string


class Game:
    def __init__(self):
        self.score = 0

    def prepare_cards(self, card):
        cards = []
        for i in range(len(card.back_face)):
            cards.append(card.back_face[i])
            cards.append(card.front_face[i])
        return cards

    def set_board(self, cards):
        for i in range(cards.back_face):
            if i % 3 == 0:
                print('')
            print(f"[ {cards.back_face[i]} ]", end="  ")
        print('')

    def is_pair(self, pair_found):
        for x in self.cards:
            if x == pair_found:
                self.cards[x] = ' '
        pass






