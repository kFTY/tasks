# 作业： 对给出的大偶数，验证哥德巴赫猜想
import math

# 判断一个数是不是质数
def isPrime(n):
    if n < 3:
        return False  # 小于3的不用算了
    # 尝试能不能被2，3，4，5，，整除，sqrt为了去重复
    for x in range(2, int(math.sqrt(n)) + 1):  
        if n % x == 0:
            return False
    # 没有整除说明是质数
    return True

# 列出所有n以内的质数
def listPrimes(n):
    L1 = []
    for x in range(3, n, 2):
        if isPrime(x):
            L1.append(x)
    return L1


# 验证哥德巴赫猜想
def checkGB(n):
    #  哥德巴赫猜想只对大偶数
    if n % 2 != 0 or n < 4:
        print ("非大偶数")
    primelist = listPrimes(n)
    # 如果n-x也是质数，那么n确实是x和n-x两个质数的和
    for x in primelist:
        if n - x in primelist:
            return x, n - x


print (checkGB(123456))
