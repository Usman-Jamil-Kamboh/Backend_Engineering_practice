class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            second_num = target - nums[i]

            if second_num in seen :
                return [i , seen[second_num]]

            
            seen[nums[i]] = i 



        

       





