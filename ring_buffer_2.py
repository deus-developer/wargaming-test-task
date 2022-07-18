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

# Реализация циклического буфера с помощью связанного списка.
from __future__ import print_function


class RingBufferNode(object):
    """Элемент связанного списка"""

    __slots__ = ('next_node', 'value')

    def __init__(self, next_node=None, value=None):
        self.next_node = next_node
        self.value = value


class RingBuffer(object):
    """Circular buffer"""

    __slots__ = ('_head', '_tail', '_count', '_size')

    def __init__(self, buffer_size):
        if buffer_size < 1:
            raise ValueError('buffer size must be greater than 0')
        self._size = buffer_size
        self._count = 0

        self._head = None
        self._tail = None

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
        element_node = RingBufferNode(self._tail, element)

        if self._tail is None:
            self._tail = element_node
            self._head = element_node

        self._head.next_node = element_node
        self._head = element_node
        self._count += 1

        if self._count <= self._size:
            return

        self.pop()

    def pop(self):
        """Получает и удаляет самый старый элемент буфера"""
        if self._count == 0:
            raise IndexError('Buffer is empty')

        self._count -= 1
        tail_node_value = self._tail.value
        self._tail = self._tail.next_node
        self._head.next_node = self._tail
        return tail_node_value

    def get(self):
        """Получает самый старый элемент буфера"""
        if self._count == 0:
            raise IndexError('Buffer is empty')
        return self._tail.value

    def __iter__(self):
        """Итерирует содержимое буфера"""
        if self._count == 0:
            return
        yield self._tail.value
        tail = self._tail.next_node
        while tail != self._head.next_node:
            yield tail.value
            tail = tail.next_node

    def clear(self):
        """Очищает буфер"""
        self._count = 0
        self._head = None
        self._tail = None


if __name__ == '__main__':
    test_buffer = RingBuffer(buffer_size=7)
    for _ in range(10):
        test_buffer.append(_)
        print(list(test_buffer))

    for _ in range(5):
        test_buffer.pop()
        print(list(test_buffer))
