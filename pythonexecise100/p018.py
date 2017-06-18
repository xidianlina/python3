'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

def sn():
    from functools import reduce
    Tn=0
    Sn=[]
    n=int(input('n = '))
    a=int(input('a = '))

    for cnt in range(n):
        Tn=Tn+a
        a=a*10
        Sn.append(Tn)
        print(Tn)

    Sn=reduce(lambda x,y:x+y,Sn)
    print('计算和为:',Sn)

def sn2():
    from functools import reduce
    Sn=0
    n=int(input('n = '))
    a=int(input('a = '))
    list=[]
    for i in range(1,n+1):
        list.append(int("{}".format(a)*i))
        Sn = reduce(lambda x,y:x+y, list)
    print('计算和为:',Sn)
            
