import math

def factorize(n):
    val = 1
    for i in range(n, 1, -1):
        val *= i
    return val

def getPrimes(n):
    primes = []
    primes.append(2)
    primes.append(3)
    for i in range(1,n):
        for j in range(2,int(math.sqrt(i))+1):
            #print("checking {} % {}".format(i, j))
            if i % j == 0:
                break
            if j == (int(math.sqrt(i))):
                primes.append(int(i))
    return primes

primes = getPrimes(7920)
num_cases = int(input())

for i in range(num_cases):
    num = int(input())
    factored_val = int(factorize(num))
    exponent = 0
    exponents = []
    for prime in [x for x in primes if x <= num][::-1]:
        while prime <= factored_val:
            print('Checking {} against {}'.format(factored_val, prime))
            if factored_val % prime == 0:
                print("{} % {} == 0".format(factored_val, prime))
                exponent += 1
                factored_val = int(factored_val / prime)
                if factored_val == 1:
                    exponents.append(exponent)
            else:
                if exponent != 0:
                    print("appending {}".format(exponent))
                    exponents.append(exponent)
                exponent = 0
                break
    print([x for x in exponents if x != 0])
