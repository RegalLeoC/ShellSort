from dtslib import *
import random

test = random.sample(range(1,20), 19)
# test = [33, 31, 40, 8, 12, 17, 25, 42]

print("*******Original********")
print(test)

print("*******Ordenado Shell Sort******")
test = shell_sort(test)
print(test)
