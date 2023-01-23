# 2. Доработать функцию flat_generator,
# Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
# Функция test в коде ниже также должна отработать без ошибок.

import types

def flat_generator(list_of_lists):
    sublist_index = 0
    while sublist_index < len(list_of_lists):
        sublist_index += 1
        item_index = 0
        sublist = list_of_lists[sublist_index - 1]
        while item_index < len(sublist):
            item = list_of_lists[sublist_index - 1][item_index]
            yield item
            item_index += 1

list_ = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

for i in flat_generator(list_):
    print(i)


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()



