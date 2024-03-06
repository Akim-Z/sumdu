#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import math
import random

def calc_z(a):
	return math.cos(a) + math.cos(2 * a) + math.cos(6 * a) + math.cos(7 * a)

def calc_y(n=random.randint(10, 30)):
	y = 1
	for i in range(1, 2 * n - 1, 2):
		y *= i
	return y

y = calc_y()

print("Результат роботи обчислення:", y)

print("Введіть значення a у радіанах для обчислення виразу: ", end="")

a = float(input())

result = calc_z(a)

print("Результат обчислення:", result)
