def get_count_char(str_: chr) -> dict:
    str_ = "".join(str_.lower().split())
    dictionary_of_letters = {}
    for letter in str_:
        if letter.isalpha():
            if letter not in dictionary_of_letters:
                dictionary_of_letters[letter] = 1
            else:
                dictionary_of_letters[letter] += 1
    return dictionary_of_letters


def new_dictionary(dictionary: dict) -> dict:
    count_of_letters = sum(dictionary.values())
    new_dict = {}
    for key in dictionary:
        new_dict[key] = f'{(dictionary[key] / count_of_letters) * 100:.3f}'
    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(new_dictionary(get_count_char(main_str)))
