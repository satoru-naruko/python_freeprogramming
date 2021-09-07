#!/usr/bin/env python3

list = [1, 10, 100, 49, 32]

print (len(list))

s = ['a','b','c','d','e','f','g']

print (s[2:5])

s[2:4] = []
print(s)

# empty list
s[:] = []

s = ['a','b','c','d','e','f','g']

del s[3]

print(s)

z = s.copy()

print(z)
