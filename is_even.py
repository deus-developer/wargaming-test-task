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

# Определение чётности числа, через проверку последнего бита.
# Если последний бит не установлен, то число чётное.
# Этот способ чуть медленнее, чем получение остатка от деления,
# а также чуть менее понятен.
#
# Уменьшение скорости связано с тем, что числа в python - это объекты,
# но, например, в компилируемых языках, такой метод был бы быстрее,
# при условии, что компилятор не будет оптимизировать эту функцию.
# Например GCC преобразует взятие остатка от деление в проверку последнего бита,
# а CLang делать это не будет.
#
# В случае с python, лучше использовать вариант с проверкой остатка от деления,
# так как он более читабелен.


def is_even(value):
    """Returns True if the number is even.

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return value & 1 == 0


if __name__ == '__main__':
    for number in range(1, 11):
        if is_even(number):
            print(number, 'is even')
        else:
            print(number, 'is odd')
