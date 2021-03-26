from Game import Game


def set_board(game, flipped_cards=[]):
    for i in range(len(game.cards)):
        if i % 3 == 0:
            print('')

        card = game.cards[i]
        card_face = card.front_face if card in flipped_cards else card.visible_face

        print(f"[ {card_face} ]", end="  ")
    print('')


game1 = Game()
game1.start()
last_event = None


def ask_for_card():
    if last_event == 'FIRST_CARD_PICKED':
        return input('Select the second card...').upper()
    return input('Select a card...').upper()


while True:
    set_board(game1)
    letter = ask_for_card()

    if letter == 'Q':
        break
    elif game1.score == 6:
        print('you won!')
        break

    state = game1.flip(letter)
    last_event = state.event

    # During the first turn we don't need to do anything
    if state.event == 'FIRST_CARD_PICKED':
        continue

    if state.event == 'INVALID_MOVE':
        print(f'Card {state.event_cards[0].back_face} is already opened!')
        continue

    set_board(game1, state.event_cards)
    if state.event == 'TURN_ENDED':
        print('Try again!')
    elif state.event == 'PAIR_FOUND':
        print('pair found!')
        print(f'Score: {game1.score}')



