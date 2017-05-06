import numpy as np

'''
使用随机的方法，尝试在找出一个答案
对于16宫格，一共有16！== 2E13 种情况
耗时太长，跑不出来
'''


def SqueredUp(n):
    # 生成 1,2,3,4,5,6,7,8,9
    numlist = np.arange(n * n) + 1
    # 初始化i
    i = 0
    while True:
        i += 1
        if i % 1000000 == 0:
            print ("Searched %i M" % (i/1000000))
        # 实在跑不出来就算了
        if i >= 100000000000:
            print ("I give up...")
            break
        # 尝试一个随机的排序
        np.random.shuffle(numlist)
        # 生成九宫格
        a = np.reshape(numlist, (n, n))
        # 判断各行求和是否相同，不同的话中断此组合
        sumX = np.sum(a, axis=0)
        if not max(sumX) == min(sumX):
            continue
        # 判断各行求和是否和前值相同，不同的话中断此组合
        sumY = np.sum(a, axis=1)
        if not max(sumY) == min(sumY) == max(sumX):
            continue
        # 主对角线的和
        traceValue = np.trace(a)
        # 判断主对角线是否相同，不同的话中断此组合
        if traceValue != max(sumX):
            continue
        # 副对角线的和
        a90 = np.rot90(a)
        traceValue2 = np.trace(a90)
        # 判断副对角线是否相同，不同的话中断此组合
        if traceValue2 != max(sumX):
            continue
        # 输出结果
        print ("Found a result: sum %d in all lines" % traceValue)
        print (a)
        break


SqueredUp(3)
