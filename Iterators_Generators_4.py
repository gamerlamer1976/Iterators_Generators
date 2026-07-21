import types


def flat_generator(list_of_list):
    # Проходим по всем элементам переданного списка
    for item in list_of_list:
        # Проверяем, является ли текущий элемент вложенным списком
        if isinstance(item, list):
            # Если да, рекурсивно вызываем flat_generator для этого элемента
            # и используем yield from для делегирования возврата значений
            yield from flat_generator(item)
        else:
            # Если это базовое значение (не список), возвращаем его
            yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print("Тест 4 пройден успешно!")


if __name__ == '__main__':
    test_4()
