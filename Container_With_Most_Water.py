class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1 
        area = 0

        while left < right :
            width = right - left
            length = min(height[left] , height[right])
            total_area = width * length
            area = max(area , total_area)
            
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return area

        
