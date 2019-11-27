#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-11-25 13:18:50
# @Author  : Dong (dongwei@tamu.edu)
# @Link    : https://github.com/tomatoJr
# @Version : 1.0.0

import random
import time
from collections import OrderedDict
import math


class MaxHeap:
    def __init__(self):
        self.D = dict()
        self.H = dict()
        self.pos = 0

    def swap(self, x, y):
        self.H[x], self.H[y] = self.H[y], self.H[x]
        self.D[x], self.D[y] = self.D[y], self.D[x]

    def insert(self, index, value):
        self.H[self.pos] = index
        self.D[self.pos] = value
        self.pos += 1
        i = len(self.H)-1
        while i >= 1 and self.D[math.floor((i-1)/2)] < self.D[i]:
            self.swap(math.floor((i-1)/2), i)
            i = math.floor((i-1)/2)

    def buildHeap(self, index_array, value_array):
        for i in range(len(index_array)):
            self.insert(index_array[i], value_array[i])

    def maximum(self):
        return self.H[0], self.D[0]

    def delete(self, value):
        i = list(self.H.values()).index(value)

        if i == len(self.H)-1:
            del self.H[i]
            del self.D[i]
            self.pos -= 1
            return

        self.swap(i, len(self.H)-1)
        del self.H[len(self.H)-1]
        del self.D[len(self.D)-1]
        self.pos -= 1
        if i >= 1 and self.D[i] > self.D[math.floor((i-1)/2)]:
            while i >= 1 and self.D[i] > self.D[math.floor((i-1)/2)]:
                self.swap(i, math.floor((i-1)/2))
        else:
            while 2*i+2 <= len(self.H)-1 and (self.D[i] < self.D[2*i+2] or self.D[i] < self.D[2*i+1]):
                if self.D[2*i+2] > self.D[2*i+1]:
                    self.swap(i, 2*i+2)
                    i = 2*i+2
                else:
                    self.swap(i, 2*i+1)
                    i = 2*i+1

    def heapSort(self):
        n = len(self.H)
        for i in range(n, -1, -1):
            self.heapify(n, i)
        for i in range(n-1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and self.D[i] < self.D[left]:
            largest = left
        if right < n and self.D[largest] < self.D[right]:
            largest = right
        if largest != i:
            self.swap(i, largest)
            self.heapify(n, largest)


if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7, 9, 4, 15]
    # array = [10, 5, 3, 2, 4]
    # array = [4, 10, 3, 5, 1]
    # array = [7, 10, 20, 3, 4, 49, 50]
    array0 = [i for i in range(len(array))]
    heap = MaxHeap()
    heap.buildHeap(array0, array)

    # print(heap.H)
    # for i in heap.H:
    #     print(array[i])
    print(heap.H.values())
    print(heap.D.values())
    # print(heap.maximum())

    heap.delete(5)
    print(heap.H.values())
    print(heap.D.values())
