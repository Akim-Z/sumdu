#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import random

def calc_y(n=random.randint(10, 30)):
	y = 1
	for i in range(1, 2 * n - 1, 2):
		y *= i
	return y
