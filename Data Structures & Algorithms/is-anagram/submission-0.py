class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S=[]
        for i in (s):
            S.append(i)
        T=[]
        for i in (t):
            T.append(i)

        list(set(S))
        S=sorted(S)
        list(set(T))
        T=sorted(T)
        if T==S:
            return True
        else:
            return False
