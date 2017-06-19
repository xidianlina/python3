'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

def inp(numbers,l):
    for i in range(l):
        numbers.append(int(input('输入一个数字:')))

p=0

def arr_max(array):
    max=0
    for i in range(1,len(array)-1):
        p=i
        if array[p]>array[max]:
            max=p
    k=max
    array[0],array[k]=array[k],array[0]

def arr_min(array):
    min=0
    for i in range(1,len(array)-1):
        p=i
        if array[p]<array[min]:
            min=p
        l=min
        array[len(array)-1],array[l]=array[l],array[len(array)-1]

def outp(numbers):
    for i in range(len(numbers)):
        print(numbers[i])

if __name__=='__main__':
    array=[]
    inp(array,6)
    arr_max(array)
    arr_min(array)
    print('计算结果:')
    outp(array)
