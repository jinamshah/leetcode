class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        for i in range(num_rows):
            last_element = matrix[i][-1]
            if target == last_element:
                return True
            elif target < last_element:
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        # todo: binary search here
                        return True
            elif target > last_element:
                continue
                