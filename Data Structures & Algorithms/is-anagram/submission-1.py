class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the string
        # check if both lists are equal
        s_list = list(s)
        t_list = list(t)
        
        str(s_list.sort())
        str(t_list.sort())
        return s_list == t_list