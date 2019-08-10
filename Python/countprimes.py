#!/usr/bin/python3

nums = 100
primeCount = 0

for i in range(nums):
    if isprime(i):
        primeCount += 1

def isprime(num):
    for a in range(sqrt(num)):
        if num % a == 0:
            return False
    return True
