class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        for i in range(num_rows):
            last_element = matrix[i][-1]
            if target == last_element:
                return True
            elif target < last_element:
                left,right = 0, len(matrix[i]) -1
                while left <= right:
                    pivot_idx = (left+right)//2
                    pivot_element = matrix[i][pivot_idx]
                    if target == pivot_element:
                        return True
                    elif target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
                # for j in range(len(matrix[i])):
                #     if target == matrix[i][j]:
                #         # todo: binary search here
                #         return True
            elif target > last_element:
                continue
                