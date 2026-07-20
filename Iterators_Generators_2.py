import types


def flat_generator(list_of_lists):
    # Проходим по каждому вложенному списку в основном списке
    for nested_list in list_of_lists:
        # Проходим по каждому элементу внутри вложенного списка
        for item in nested_list:
            # Возвращаем элемент и приостанавливаем выполнение функции
            yield item


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
    print("Тест 2 пройден успешно!")


if __name__ == '__main__':
    test_2()
