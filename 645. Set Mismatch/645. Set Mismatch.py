# used pure mathematics 
# [1,2,2] => sum=5 setsum=3 so subtracting it will give us the number plus ideally the sum should be 6 so 6-setsum gives the desired value



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), (len(nums) *(len(nums)+1))//2- sum(set(nums))]
        