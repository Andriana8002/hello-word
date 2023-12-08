# рандом
from random import randint

x = [randint(1,100) for i in range(5)]

for i in range(1,101):
    print(i, x.count(i))    