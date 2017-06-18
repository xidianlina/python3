'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

'''

s=input('请输入大于10的数字:')

if(len(s)>0)and(len(s)<=5):
    print("%s 是 %d 位数" %(s, len(s)))
    newstr=str(s)[::-1]
    for i in newstr:
        print(i,end='')
