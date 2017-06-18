'''
题目：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
'''

import time

myDict={1:'a',2:'b',3:'c',4:'d',5:'e'}
for key,value in dict.items(myDict):
    print(key,value)
    time.sleep(1)
