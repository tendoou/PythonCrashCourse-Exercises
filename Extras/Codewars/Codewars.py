import string


def is_uppercase(letters):
    letters = letters.replace(' ', '')
    for letter in letters:
        if letter in list(string.ascii_lowercase):
            return False
    return True

