class Solution(object):
    def reverse(self, x):
        new_num=x
        rev_int=0
        if x<0:
            x=-x
        while (x>0):
            rev_int=rev_int*10+x%10
            x=x//10
        if rev_int > (2** 31 -1) or rev_int < -(2 ** 31):
            return 0
        elif new_num<0:
            return - rev_int
        return rev_int
        
        
sol = Solution()
rev=sol.reverse(9329239229)
print(rev)

