'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
'''

def sq(x):
    return x*x

print('如果输入的数字小于 50，程序将停止运行。')

while True:
    num=int(input('请输入一个数字：'))
    print('运算结果为: %d' % (sq(num)))
    if sq(num)<50:
        break
