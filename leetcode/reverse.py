'''
Reverse Integer

Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x>0:
            s=1
        elif x<0:
            s=-1
        else:
            s=0
        r=s*x
        y=str(r)[::-1]
        r=int(y)
        return (r<2**31)*s*r
        
res=Solution.reverse(-321)
print(res)
