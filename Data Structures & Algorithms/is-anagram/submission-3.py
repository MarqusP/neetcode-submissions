class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorting each list is O(logn)
        # comparing each letter is O(n)
        return sorted(s) == sorted(t)