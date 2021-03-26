from GameState import GameState
from Memorama import Card
import random
import string


class Game:
    def __init__(self):
        self.score = 0
        self.cards = []

    def get_all_front_faces(self):
        emoji = [ "👻","💩","🦊","🚀","🧠" ,"🤠"]

        all_front_faces = emoji + emoji
        random.shuffle(all_front_faces)
        return all_front_faces

    def start(self):
        front_faces = self.get_all_front_faces()
        for i in range(len(front_faces)):
            front_face = front_faces[i]
            back_face = string.ascii_uppercase[i]
            self.cards.append(Card(back_face, front_face))

    def flip(self, chosen_card):
        for card in self.cards:
            if card.back_face == chosen_card:
                if card.is_flipped:
                    return GameState('INVALID_MOVE', [card])
                else:
                    card.flip()
        return self.evaluate_board()

    def get_revealed_cards(self):
        flipped_cards = []
        for card in self.cards:
            if card.is_flipped and not card.is_paired:
                flipped_cards.append(card)
        return flipped_cards

    def evaluate_board(self):
        flipped_cards = self.get_revealed_cards()

        if len(flipped_cards) < 2:
            # an intermediate event with the flipped cards
            return GameState('FIRST_CARD_PICKED', flipped_cards)

        piece1 = flipped_cards[0]
        piece2 = flipped_cards[1]

        if piece1.matches(piece2):
            piece1.is_paired = True
            piece2.is_paired = True
            self.score += 1
            return GameState('PAIR_FOUND', [piece1, piece2])
        else:
            piece1.flip()
            piece2.flip()
            return GameState('TURN_ENDED', [piece1, piece2])