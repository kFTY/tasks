from itertools import permutations


def product(num):
    strnum = str(num)
    result = 0
    for i in range(1, len(strnum)):
        parta = strnum[:i]
        partb = strnum[i:]
        r = int(parta) * int(partb)
        if r > result:
            result = r
    return (result)


def product_2(num):
    result = 0
    for p in permutations(str(num)):
        mixnumber = "".join(p)
        r = product(mixnumber)
        if r > result:
            result = r
    return (result)


print (product(1234))
print (product(12345))
print (product_2(123456))
