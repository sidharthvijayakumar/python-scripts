class Solution(object):
    def twoSum(self, nums, target):
        #brute force
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if (nums[i]+nums[j]==target) and i!=j:
        #             return [i,j]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i,j]           

            
sol= Solution()
res=sol.twoSum([3,2,4],6)
print(res)