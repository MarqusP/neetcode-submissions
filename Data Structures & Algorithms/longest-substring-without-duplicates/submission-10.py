class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        new_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in new_set:
                new_set.remove(s[l])
                l += 1
            new_set.add(s[r])
            longest = max(longest, r - l + 1)

        return longest
        




            
            
            



