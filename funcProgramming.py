#!/usr/bin/env python3

from termcolor import colored

print("funcPrograming start")


def test_func(str):
    print(colored('test', 'yellow'))


test_func("-----!!-----")

num = 123

print(isinstance(num, int))  # true
print(isinstance(num, str))  # false


def funcA(name):
    print("name is {}".format(name))


funcA("aaabbbccc")
