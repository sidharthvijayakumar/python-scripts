class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (nums[i]+nums[j]==target) and i!=j:
        #             return [i,j]
        #better than normal brute force
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if (nums[i]+nums[j]==target):
        #             return [i,j]  

       #decalre a dictonary 
        values=dict()
        #iterate through the nums list where i is the index and element is the value
        for i, element in enumerate(nums):
            var=target-element
            if var in values:
                #returns values[var] if present would be the difference between target & the element this values[var] 
                #will give the index postion and the current index of i
                return [values[var],i]
            #this appends the dictonary with the key element and adds the value as i which is its corresponding index in the list
            values[element]=i
        return []

sol= Solution()
res=sol.twoSum([3,2,4],7)
print(res)