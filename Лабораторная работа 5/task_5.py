from random import sample
import string


def get_random_password(n: int = 8) -> str:
    return ''.join(sample(string.ascii_lowercase + string.ascii_uppercase + string.digits,
                          k=n))


print(get_random_password())
