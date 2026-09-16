class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_water = 0

        # the height is the minimum value between two heights
        # the width is the distance between two bars 

        # if l > r, that is the most water the container can contain given the value for index r

        # if r > l, there can be potentially values greater than l that can produce a bigger
        # containment of water

        while l < r:
            curr_max = (r - l) * min(heights[l], heights[r])
            max_water = max(max_water, curr_max)

            if heights[r] >= heights[l]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return max_water

            
        

            
            
