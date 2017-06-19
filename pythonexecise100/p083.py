'''
题目：求0—7所能组成的奇数个数。
'''

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print(sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print('sum = %d' % sum)
    
'''
sum=4; 表示1位数的情况下，有4种，s=4也是这个意思.

j=2,表示2位数的情况下，有7*4种,因为个位是奇数,十位不为0.
j=3,表示3位数情况下,有7*(8)*4,表示百位部位0，个位数是奇数，十位数0~7任意
j=4, = 7*(8)*8*4...
j=5 , =7*(8)*8*8*4

就这样,每次插入一个8到乘积序列中.
'''