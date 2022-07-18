# coding=utf-8
# https://en.wikipedia.org/wiki/Radix_sort

from random import randint


def radix_sort(array, copy=False):
    if copy:
        array = array[:]
    buckets = [[] for i in range(10)]
    max_length = False
    tmp = -1
    placement = 1
    while not max_length:
        max_length = True

        for i in array:
            tmp = i // placement
            buckets[tmp % 10].append(i)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for bucket in buckets:
            for i in bucket:
                array[a] = i
                a += 1
            del bucket[:]
        placement *= 10
    return array


if __name__ == '__main__':
    array = [randint(0, 100) for _ in range(10000000)]
    radix_sort(array, True)
