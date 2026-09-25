class Solution:
    def findBuildings(self, h: List[int]) -> List[int]:
        n=len(h)
        ans=[n-1]
        pmax=h[n-1]
        for i in reversed(range(n)):
            if h[i]>pmax:
                pmax=h[i]
                ans.append(i)
        return sorted(ans,reverse=False)


        