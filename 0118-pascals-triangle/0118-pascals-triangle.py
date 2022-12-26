class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        for cnt in range(2, numRows):
            prevRow = ans[cnt-1]
            temp = [1]
            for i in range(len(prevRow)-1):
                temp.append(prevRow[i]+prevRow[i+1])
            temp.append(1)
            ans.append(temp)
        return ans