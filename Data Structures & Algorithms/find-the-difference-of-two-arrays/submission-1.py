class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[[],[]]
        done1=[]
        done2=[]
        for i in nums1:
            if i not in nums2 and i not in done1:
                ans[0].append(i)
                done1.append(i)
        for i in nums2:
            if i not in nums1 and i not in done2:
                ans[1].append(i)
                done2.append(i)
        return ans