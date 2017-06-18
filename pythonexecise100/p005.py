'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''

# 利用冒泡排序方法
def Sort(list):
    n = len(list)
    for i in range(1, n):
        for j in range(1, n - i + 1):
            if list[j - 1] > list[j]:
                list[j - 1], list[j] = list[j], list[j - 1]
            print(list)
    for i in range(0, n):
        print(list[i],end=' ')

# 读入数据
def inputData():
    list_first = []
    while True:
        a = input("please input num:".strip())
        if len(a) == 0:
            return list_first
        else:
            list_first.append(int(a))

if __name__ == '__main__':
    lt = inputData()
    print(lt)
    Sort(lt)
