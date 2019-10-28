#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3

def sort(data):
    absdata = [abs(x) for x in data]
    return sorted(absdata)

print(sort(data))