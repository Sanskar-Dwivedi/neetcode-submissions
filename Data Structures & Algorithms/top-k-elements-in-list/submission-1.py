class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsSet=list(set(nums))
        NumDict={}

        for num in numsSet:
            
            NumDict[num]=nums.count(num)
        ans=dict(sorted(NumDict.items(), key=lambda item: item[1],reverse=True))
        i=0
        final=[]
        for val,feq in ans.items():
            if i<k:
                final.append(val)
            i+=1
                
        return(final)