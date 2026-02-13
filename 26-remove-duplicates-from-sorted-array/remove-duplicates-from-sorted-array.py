class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       i=0
       n=len(nums)
       for k in range(1,n):
         if nums[k]!=nums[i]:
            nums[i+1]=nums[k]
            i+=1
       return i+1

