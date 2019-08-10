import itertools

def diff(l):
    subs = []
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[j] - l[i] in subs:
                return False
            subs.append(l[j] - l[i])
    return True

def permute(iterator, r=None, k=1, n=1):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

    begin_vals = [1, 2, 4, 8, 13, 21, 31, 47, 62, 83]
    pool = tuple(iterator)
    #n = len(pool)
    r = n if r is None else r
    print("pool: {}, n: {}, r: {}".format(pool, n, r))
    if r > n:
        print("r: {} > n: {}".format(r,n))
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    count = 0
    print("indicies: {}, cycles: {}, count: {}".format(indices, cycles, count))
    yield tuple(begin_vals[i] for i in indices[:r])
    print("tuple: {}".format(tuple(begin_vals[i] for i in indices[:r])))
    while n and count < k:
        print("while n: {}".format(n))
        for i in reversed(range(r)):
            print("for i in reversed(range(r)): {}".format(list(reversed(range(r)))))
            cycles[i] -= 1
            print("cycles[i] -= 1: {}".format(cycles[i]))
            if cycles[i] == 0:
                print("if cycles[i] == 0:")

                indices[i:] = indices[i+1:] + indices[i:i+1]
                print("indices[i:] = indices[i+1:] + indices[i:i+1]: {}".format(indices[i:]))
                cycles[i] = n - i
                print("cycles[i] = n - i : {}".format(cycles[i]))
            else:
                print("else:")
                j = cycles[i]
                print("j = cycles[i]: {}".format(j))
                indices[i], indices[-j] = indices[-j], indices[i]
                print("indices[i], indices[-j] = indices[-j], indices[i]: {}".format(indices[i], indices[-j]))
                if diff(list(tuple(pool[i] for i in indices[:r]))):
                    count += 1
                    yield tuple(pool[i] for i in indices[:r])
                print("yeild tuple(pool[i] for i in indices[:r]): {}".format(tuple(pool[i] for i in indices[:r])))
                break
        else:
            return

def easy_permute(iterable, r=None, k=1, n=1):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in [x for x in itertools.product(range(n), repeat=r) if diff(x)]:
        if len(set(indices)) == r:
            print("indices: {}".format(indices))
            yield tuple(pool[i] for i in indices)

num_cases = int(input())

for i in range(num_cases):
    vals = input()
    n = int(vals.split()[0])
    s = int(vals.split()[1])
    k = int(vals.split()[2])

    perms = easy_permute(range(1,n+1), s, k, n)

    mixed_perms = [x for x in perms if diff(x)]
    #print(mixed_perms)

    #print(mixed_perms[k-1])
