class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count={"1":0,
                "0":0}
        for i in s:
            if i=="1":
                count["1"]+=1
            else:
                count["0"]+=1
        onerem=count["1"]
        ans=""
        while count["1"]>1:
            ans += "1"
            count["1"]-=1
        while count["0"]>0:
            ans+="0"
            count["0"]-=1
        ans+="1"
        return ans
