class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        duplicates=[]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                duplicates.append(nums[i])
        return duplicates
