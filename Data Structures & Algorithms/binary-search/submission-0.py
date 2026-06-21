class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        def BinaryFinder(nums,target,left,right):

            mid=(left+right)//2

            if left>right:
                return -1
            elif nums[int(mid)]==target:
                return int(mid)
            elif nums[int(mid)]>target:
                return BinaryFinder(nums,target,left,int(mid)-1)
            elif nums[int(mid)]<target:
                return BinaryFinder(nums,target,int(mid)+1,right)
        return BinaryFinder(nums,target,left,right)
