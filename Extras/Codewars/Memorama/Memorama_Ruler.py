from Memorama import Card
import random
import string


class Game:
    def __init__(self):
        self.score = 0

    def prepare_cards(self, back_faces, front_faces):
        cards = []
        for i in range(len(back_faces)):
            cards.append(Card(back_faces[i], front_faces[i]))
        return cards

    def set_board(self, cards):
        for i in range(len(cards)):
            if i % 3 == 0:
                print('')
            print(f"[ {cards[i].visible_face} ]", end="  ")
        print('')

    def flip(self, chosen_card):
        for card in cards:
            if card.back_face == chosen_card:
                if card.is_flipped:
                    card.visible_face = card.back_face
                else:
                    card.visible_face = card.front_face

                card.is_flipped = not card.is_flipped
        return cards

    def is_pair(self, cards):
        flipped_cards = []
        for card in cards:
            if card.is_flipped:
                flipped_cards.append(card.visible_face)
                if len(flipped_cards) == 2:
                    piece1 = flipped_cards[0]
                    piece2 = flipped_cards[1]
                    if piece1 == piece2:
                        print('you found a pair')
                    else:
                        for x in cards:
                            x.visible_face = x.back_face





emoji = [
  "👻",
  "💩",
  "🦊",
  "🚀",
  "🧠" ,
  "🤠"]

all_front_faces = emoji + emoji
random.shuffle(all_front_faces)
all_back_faces = "ABCDEFGHIJKL"
game1 = Game()
cards = game1.prepare_cards(all_back_faces, all_front_faces)
print(game1.set_board(cards))
game1.flip('A')
game1.flip('B')
print(game1.set_board(cards))
game1.is_pair(cards)
print(game1.set_board(cards))
