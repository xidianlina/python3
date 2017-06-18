'''
题目：统计 1 到 100 之和。
'''

def sum1():
    tmp=0
    for i in range(1,101):
        tmp+=i

    print('The sum is %d'%tmp)

def sum2():
    from functools import reduce
    l=[]
    for i in range(1,101):
        l.append(i)
    s=reduce(lambda x,y:x+y,l)
    print('The sum is %d'%s)
