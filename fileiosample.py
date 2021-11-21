import importlib

test_str = """\
aaaAAA
BBBbbb
CCCccc
DDD
EEE
"""

with open('my_test.txt', 'w') as f1:
    f1.write(test_str)

with open('my_test.txt', 'r') as f:
    while True:
        chunk = 2
        line = f.readline()
        print(line, end='')
        if not line:
            break

