from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        multiThis=[]
        for j in range(len(nums)):
            for i in range(len(nums)):
                if j==i:
                    continue
                multiThis.append(nums[i])
            ans.append(reduce(lambda a, b: a * b, multiThis))
            multiThis=[]
        return (ans)

