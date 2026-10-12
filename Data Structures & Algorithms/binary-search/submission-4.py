class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = low + 1
            elif nums[mid] > target:
                high = high - 1
            else:
                return mid
        
        return -1
