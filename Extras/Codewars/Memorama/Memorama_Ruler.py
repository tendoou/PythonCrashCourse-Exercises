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
        print(front_faces)
        for i in range(len(front_faces)):
            front_face = front_faces[i]
            back_face = string.ascii_uppercase[i]
            self.cards.append(Card(back_face, front_face))

    def set_board(self):
        for i in range(len(self.cards)):
            if i % 3 == 0:
                print('')
            print(f"[ {self.cards[i].visible_face} ]", end="  ")
        print('')

    def flip(self, chosen_card):
        for card in self.cards:
            if card.back_face == chosen_card:
                if card.is_flipped:
                    print(f'{card.back_face} is already opened!')
                else:
                    card.flip()
                    print(f'{card.front_face} appeared')
        self.evaluate_board()
        # return game state

    def get_revealed_cards(self):
        flipped_cards = []
        for card in self.cards:
            if card.is_flipped and not card.is_paired:
                print(f'{card.front_face} is flipped')
                flipped_cards.append(card)
        return flipped_cards

    def evaluate_board(self):
        flipped_cards = self.get_revealed_cards()

        if len(flipped_cards) < 2:
            return

        piece1 = flipped_cards[0]
        piece2 = flipped_cards[1]

        if piece1.matches(piece2):
            print(f'{piece1.front_face} pair found')
            piece1.is_paired = True
            piece2.is_paired = True
            self.score += 1
        else:
            piece1.flip()
            piece2.flip()
            print(f'{piece1.front_face} hiding')
            print(f'{piece2.front_face} hiding')







emoji2 = [
  "👻",
  "💩",
  "🦊",
  "🚀",
  "🧠" ,
  "🤠"]

#all_front_faces = emoji + emoji
#random.shuffle(all_front_faces)
#all_back_faces = "ABCDEFGHIJKL"
game1 = Game()
game1.start()
#cards = game1.prepare_cards(all_back_faces, all_front_faces)
game1.set_board()

while True:
    letter = input('which one').upper()
    print(f'Flipeando {letter}')
    if letter == 'Q':
        break
    elif game1.score == 6:
        print('you won!')
        break
    game1.flip(letter)
    game1.set_board()
