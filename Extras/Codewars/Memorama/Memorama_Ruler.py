from Memorama import Cards
import random
import string


class GameRuler:
    def __init__(self):
        pass

    def set_board(self, all_back_faces):
        for i in range(len(all_back_faces)):
            if i % 3 == 0:
                print('')
            print(f"[ {all_back_faces[i]} ]", end='  ')

        print('')


    def is_pair(self, pair_found):
        for x in self.cards:
            if x == pair_found:
                self.cards[x] = ' '
        pass




emoji = [
  "👻",
  "💩",
  "🦊",
  "🚀",
  "🧠" ,
  "🤠"
]
all_front_faces = emoji + emoji
random.shuffle(all_front_faces)
all_back_faces = []
for i in range(12):
    all_back_faces.append(string.ascii_uppercase[i])
game1 = Cards(all_back_faces, all_back_faces)
game2 = GameRuler()
game2.set_board(all_back_faces)


