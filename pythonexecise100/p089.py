'''
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''

num=int(input("请输入一个四位整数:"))
num=str(num)
List=[]
for i in range(0,len(num)):
    a=(int(num[i])+5)%10
    List.append(a)

List[0],List[3]=List[3],List[0]
List[1],List[2]=List[2],List[1]
print(List[0]*1000+List[1]*100+List[2]*10+List[3])
