class Solution:
    def containsDuplicate(self, nums):
        Dup=set()
        for i in nums:
            if i in Dup:
                return True
            Dup.add(i)
        return False
        
solution=Solution()
nums=[1,2,3,1]
result=solution.containsDuplicate(nums)
print(result)
