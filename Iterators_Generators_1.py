class FlatIterator:
    def __init__(self, list_of_list):
        # Сохраняем исходный список списков как атрибут экземпляра
        self.list_of_list = list_of_list

    def __iter__(self):
        # Инициализируем курсоры для отслеживания текущего положения.
        # outer_cursor — индекс внешнего списка, inner_cursor — индекс внутри вложенного списка.
        self.outer_cursor = 0
        self.inner_cursor = 0
        return self

    def __next__(self):
        # Используем цикл while для обработки возможных пустых вложенных списков
        while self.outer_cursor < len(self.list_of_list):
            current_nested_list = self.list_of_list[self.outer_cursor]

            # Если внутренний курсор не вышел за пределы текущего вложенного списка
            if self.inner_cursor < len(current_nested_list):
                item = current_nested_list[self.inner_cursor]
                self.inner_cursor += 1
                return item

            # Если элементы во вложенном списке закончились, переходим к следующему
            self.outer_cursor += 1
            self.inner_cursor = 0

        # Если внешние списки закончились, возбуждаем исключение StopIteration
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("Тест 1 пройден успешно!")


if __name__ == '__main__':
    test_1()
