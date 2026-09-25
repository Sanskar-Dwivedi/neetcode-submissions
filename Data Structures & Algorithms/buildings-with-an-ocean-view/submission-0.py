class Solution:
    def findBuildings(self, h: List[int]) -> List[int]:
        
        n=len(h)
        ans=[n-1]
        pmax=h[n-1]

        for i in reversed(range(n)):
            if h[i]>pmax:
                pmax=h[i]
                ans.append(i)
                print(h[i] , ans)
            print(h[i] , ans,"out")

        return sorted(ans,reverse=False)


        