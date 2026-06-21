class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        inhand={
            5:0,
            10:0,
            20:0
        }

        for i in bills:
            if i == 5:
                inhand[5]+=1
            elif i==10:
                if inhand[5]==0:
                    return False
                inhand[10]+=1

                inhand[5]-=1
            else:
                if inhand[10]>0 :
                    if inhand[5]>0: 
                        inhand[10]-=1
                        inhand[5]-=1
                    else:return False

                else:
                    if inhand[5]<3:
                        return False
                    inhand[5]-=3
        return True
        