from dtslib import *
import random

test = random.random()  # Sensitive


print("*******Original********")
print(test)

print("*******Ordenado Shell Sort******")
test = shell_sort(test)
print(test)
