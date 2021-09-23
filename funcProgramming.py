#!/usr/bin/env python3

print("funcPrograming start")


def test_func(str):
    print(str)


test_func("-----!!-----")

num = 123

print(isinstance(num, int))  # true
print(isinstance(num, str))  # false


def funcA(name):
    print("name is {}".format(name))


funcA("aaabbbccc")
