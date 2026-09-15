class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = 0
        res = []
        sort = sorted(nums)

        for i, a in enumerate(sort):

            if a > 0:
                break

            if i > 0 and a == sort[i - 1]:
                continue
           
            l, r = i + 1, len(nums)-1
            while l < r:
                total = sort[i] + sort[l] + sort[r]
                if total > 0:
                    r = r - 1
                elif total < 0:
                    l = l + 1
                else:
                    res.append([sort[i], sort[l], sort[r]])
                    l = l + 1
                    r = r - 1
                    while sort[l] == sort[l - 1] and l < r:
                        l = l + 1
            
        return res
            
                
            
            