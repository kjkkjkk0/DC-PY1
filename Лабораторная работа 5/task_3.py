from random import randint


def get_unique_list_numbers(min=-10, max=10, count=15) -> list[int]:
    numbers_list = []
    i = 0
    while i != count:
        number = random.randint(min, max)
        if number not in numbers_list:
            numbers_list.append(number)
            i += 1
    return numbers_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
