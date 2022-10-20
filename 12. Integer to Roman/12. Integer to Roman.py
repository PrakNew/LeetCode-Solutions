#Pattern based implementation where you just subtract the number from the given list whichever is bigger until the value is equal to 0
# O(log n) solution 
class Solution:
    def intToRoman(self, num: int) -> str:
        l=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        r=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        s=''
        while num!=0:
            for ind,x in enumerate(l):
                if num>=x:
                    s+=r[ind]
                    num-=x
                    break
        return s