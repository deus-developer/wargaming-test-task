# Описание реализаций кольцевого буфера

## Использование списка и двух указателей
> Данная реализация использует список фиксированного размера,
а также два указателя для сохранения порядка элементов

## Использование связанного списка
> Данная реализация использует связанный список,
храня первый и последний элемент.
Работает крайне медленно из-за того, что производится
слишком много операций с памятью при добавлении/удалении элемента

# Производительность
Я думаю, что не стоит изобретать велосипед, ведь
есть готовое решение внутри модуля **collections** - deque

Это двухсторонняя очередь, реализованная на языке C
> Моя реализация на основе списка медленнее deque в 4.4 раз
> Реализация на основе связанного списка медленне deque в 5.3 раз
