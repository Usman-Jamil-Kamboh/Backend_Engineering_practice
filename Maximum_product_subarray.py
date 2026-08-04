class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_product = nums[0] 
        max_product = nums[0] 
        min_product = nums[0]

        for num in nums[1:]:

            old_max = max_product
            old_min = min_product

            max_product = max(num, old_max * num, old_min * num)

            min_product = min(num, old_max * num, old_min * num)

            best_product = max(best_product, max_product)
            

        return best_product 

