class Solution: 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) //2
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # Unique element is on the right side
               left = mid + 2
            else:
                # Unique element is on the left side (or at mid)
                right = mid
        
        return nums[left]
        
          
