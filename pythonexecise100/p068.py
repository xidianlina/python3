'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

if __name__=='__main__':
    n=int(input('整数 n 为:'))
    m=int(input('向后移 m 个位置为:'))

    def move(array,n,m):
        array_end=array[n-1]
        for i in range(n-1,-1,-1):
            array[i]=array[i-1]
        array[0]=array_end
        m-=1
        if m>0:
            move(array,n,m)

    number=[]
    for i in range(n):
        number.append(int(input('输入一个数字:')))

    print('原始列表:',number)

    move(number,n,m)

    print('移动之后:',number)
