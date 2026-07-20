class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_number = nums[0]
        current_number = 0 
        
        for num in nums : 
            current_number += num
            max_number = max (max_number , current_number ) 
            if current_number < 0 :
                current_number = 0 
                


        return max_number 
        
