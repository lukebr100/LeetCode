# Given an integer numRows, return the first numRows of Pascal's triangle.

# Eg:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
def pascal(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1, 1]]
    else:
        ans = [[1],[1,1]]
        for i in range(3, numRows + 1):
            appAns = [0 for k in range(i - 2)]
            appAns.append(1)
            appAns.insert(0, 1)
            ans.append(appAns)
        for i in range(2, numRows):
            for j in range(len(ans[i - 1]) - 1):
                ans[i][j + 1] = ans[i - 1][j] + ans[i - 1][j + 1]
        return ans
