class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        newS=""
        for i in range(len(s)):
            if (ord(s[i])<=57 and ord(s[i])>=48 ) or (ord(s[i])<=122 and ord(s[i])>=97) or (ord(s[i])<=90 and ord(s[i])>=65):
                newS+=(s[i])
        j=len(newS)-1
        i=0
        while i<(len(newS)):
            if i>j:
                break
            if newS[i]==newS[j]:
                j-=1
                i+=1
                continue
            else:
                return False
        return True