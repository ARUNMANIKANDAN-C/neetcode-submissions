from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # -------- Find Row --------
        top = 0
        bottom = rows - 1

        row = -1

        while top <= bottom:

            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:
                row = mid
                break

            elif target < matrix[mid][0]:
                bottom = mid - 1

            else:
                top = mid + 1

        if row == -1:
            return False

        # -------- Binary Search in Row --------
        left = 0
        right = cols - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False