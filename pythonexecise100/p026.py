'''
题目：利用递归方法求5!。
'''

def fact(x):
    sum =0
    if x==0:
        return 1;
    else:
        sum=x*fact(x-1)
    return sum

n=int(input('please enter a number:'))
for i in range(n):
    print('%d! = %d' % (i,fact(i)))
