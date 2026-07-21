class FlatIterator:
    def __init__(self, list_of_list):
        # Инициализируем стек, помещая в него итератор корневого списка
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        # Работаем до тех пор, пока стек не опустеет
        while self.stack:
            try:
                # Пытаемся получить следующий элемент из верхнего (текущего) итератора в стеке
                item = next(self.stack[-1])
            except StopIteration:
                # Если текущий итератор исчерпан, удаляем его из стека
                # и переходим на шаг назад (вверх по уровню вложенности)
                self.stack.pop()
                continue

            if isinstance(item, list):
                # Если элемент оказался списком, создаем для него итератор
                # и добавляем на вершину стека для обхода вглубь
                self.stack.append(iter(item))
            else:
                # Если это базовый элемент (не список), возвращаем его
                return item

        # Если цикл завершился и стек пуст — обход окончен
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print("Тест 3 пройден успешно!")


if __name__ == '__main__':
    test_3()
