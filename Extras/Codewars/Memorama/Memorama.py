import random
# I need to create the cards, with their properties
# like back, front and the flip action.


class Card:
    def __init__(self, back_face, front_face):
        self.back_face = back_face
        self.visible_face = back_face
        self.front_face = front_face
        self.is_flipped = False
        self.is_paired = False

    def flip(self):
        if self.is_flipped:
            self.visible_face = self.back_face
        else:
            self.visible_face = self.front_face
        self.is_flipped = not self.is_flipped

    def matches(self, card):
        return self.front_face == card.front_face




emoji = [
  "👻",
  "💩",
  "🦊",
  "🚀",
  "🧠" ,
  "🤠"
]
#all_front_faces = emoji + emoji
#random.shuffle(all_front_faces)
#all_back_faces = "ABCDEFGHIJKL"
#cards1 = Cards(all_back_faces, all_front_faces)
#print(cards1.prepare_cards())
# Then i need to assign each card an emoji and letter
# Having that i have to put all of them with the back upside
# in random order forming a board.
# When i select a card, it should turn up and let me see it's emoji
# to chose a second one and if it's a pair turn up another two cards.
# the pair of cards turned up should disappear from the board.
# If i fail, the cards must go back to the downside position.
# The game ends when all the pairs have been found and the boards is empty.
