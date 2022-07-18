# coding=utf-8

#    Copyright 2022 Artem Ukolov
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


class RingBuffer(object):
    """Circular buffer"""

    __slots__ = ('_buffer', '_head', '_tail', '_count', '_size')

    def __init__(self, buffer_size):
        if buffer_size < 1:
            raise ValueError('buffer size must be greater than 0')
        self._buffer = [None] * buffer_size
        self._head = 0
        self._tail = 0
        self._count = 0
        self._size = buffer_size

    @property
    def size(self):
        """Получить длинну буфера"""
        return self._size

    def count(self, x):
        """Кол-во элементов x в буфере"""
        return sum(1 for element in iter(self) if element == x)

    def full(self):
        """Возвращает True, если буфер заполнен"""
        return self._count == self._size

    def empty(self):
        """Возвращает True, если буфер пуст"""
        return self._count == 0

    def append(self, element):
        """Добавляет элемент в буфер"""

        # Перезапись, если буфер переполнен
        if self._count == self._size:
            self.pop()

        if self._head == self._size:
            self._head = 0

        # Добавление нового элемента
        self._buffer[self._head] = element
        self._head += 1
        self._count += 1

    def pop(self):
        """Получает и удаляет самый старый элемент буфера"""
        if self._count == 0:
            raise IndexError('Buffer is empty')

        self._count -= 1

        if self._tail == self._size - 1:  # Закольцевание
            self._tail = 0
            return self._buffer[self._size - 1]

        self._tail += 1
        return self._buffer[self._tail - 1]

    def get(self):
        """Получает самый старый элемент буфера"""
        if self._count == 0:
            raise IndexError('Buffer is empty')
        return self._buffer[self._tail]

    def __iter__(self):
        """Итерирует содержимое буфера"""
        if self._count == 0:
            return

        if self._tail < self._head:
            for index in range(self._tail, self._head):
                yield self._buffer[index]
            return

        for index in range(self._tail, self._size):
            yield self._buffer[index]

        for index in range(self._head):
            yield self._buffer[index]

    def clear(self):
        """Очищает буфер"""
        self._buffer = [None] * self._size
        self._head = 0
        self._tail = 0
        self._count = 0


if __name__ == '__main__':
    test_buffer = RingBuffer(buffer_size=7)
    for _ in range(10):
        test_buffer.append(_)
        print(list(test_buffer))

    for _ in range(5):
        test_buffer.pop()
        print(list(test_buffer))
