import random
import string


def get_random_password(n: int = 8) -> str:
    return random.sample([lower_letter for lower_letter in string.ascii_lowercase] +
                         [upper_letter for upper_letter in string.ascii_uppercase] +
                         [digit for digit in string.digits],
                         k=n)


print(''.join(get_random_password()))
