class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, a in enumerate(nums):
            if target - a in dic:
                return [dic[target - a], i]
            else:
                dic[a] = i