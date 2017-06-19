'''
题目：判断一个正整数能被几个9整除。
'''

if __name__ == '__main__':
    b=int(input('input a number:'))

    a=9
    n=1
    while (1):
        if a%b==0:
            break
        else:
            a=a*10+9
            n=n+1
    print('%d 可以被 %d 个 9 整除' % (b,n))
