import random


def get_unique_list_numbers() -> list[int]:
    numbers_list = []
    count = 0
    while count != 15:
        number = random.randint(-10, 10)
        if number not in numbers_list:
            numbers_list.append(number)
            count += 1
    return numbers_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
