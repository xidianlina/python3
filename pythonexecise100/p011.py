'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
'''

def fib(n):
    f1=1
    f2=1

    for i in range(1,int(n)):
        print('%12ld %12ld' % (f1,f2),end=' ')
        if i%3==0:
            print()
        f1=f1+f2
        f2=f1+f2

def fibs(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibs(n-1)+fibs(n-2)
    
