class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = sum(nums[:k])
        average = total / k 

        for i in range(1 , len(nums) - k +1 ):
            
            total -= nums[i-1]
            total += nums[i+k-1]

            current_average = total / k 

            average = max(average , current_average)

        return average 

        
