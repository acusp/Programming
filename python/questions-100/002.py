#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = int(input("利润："))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
bonus = 0

for idx in range(len(arr)):
    if i > arr[idx]:
        bonus += (i-arr[idx]) * rat[idx]
        i = arr[idx]

print("奖金总数为：", bonus)
