class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # figure out the range of the numbers in the row based off the first number of every row
        # binary search also within the row

        for i in matrix:
            row_len = len(i)
            # check if target greater than or equal to the range of numbers
            if target >= i[0] and target <= i[row_len - 1]:
                l = 0
                r = row_len - 1
                while l <= r:
                    mid = (l + r) // 2
                    if i[mid] > target:
                        r -= 1
                    elif i[mid] < target:
                        l += 1
                    else:
                        return True
        
        return False

            


