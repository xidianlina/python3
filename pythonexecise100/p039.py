'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

if __name__=="__main__":
    a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
    b=18
    a.append(b)
    c=a[:]
    l=len(c)
    print(c)

    for i in range(l,0,-1):
        if (b>c[i-2]):
            c[i-1] =b
            break
        else:
            c[i-1] = c[i-2]
    print(c)
