class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_table = {}
        l = 0
        res = 0
        for r in range(len(s)):
            hash_table[s[r]] = hash_table.get(s[r], 0) + 1
       
            while (r - l + 1) - max(hash_table.values()) > k:
                hash_table[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)

        return res
                
            
                