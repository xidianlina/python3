'''
题目：求100之内的素数。
'''

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
n = 0
for num in range(lower, upper + 1):
    if num >1:
        for i in range(2,int(num/2+1)):
            if num%i ==0:
                break
        else:
            print (num,end=' ')
            n += 1
print('\n',lower,'到',upper,'素数总数为',n)
