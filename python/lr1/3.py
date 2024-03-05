#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Завдання 3
# Вводиться ціле число N (1<N<9), а виводяться рядки з числами або іншими символами (*, #), 
# які утворюють визначений «рисунок» (останній задається варіантом).

n = 5

def piramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end = "")
        print()

piramid(n)
