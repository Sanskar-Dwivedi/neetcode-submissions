class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        original=len(nums)
        notOrigi=len(list(set(nums)))
        if original==notOrigi:
            return False
        else:
            return True