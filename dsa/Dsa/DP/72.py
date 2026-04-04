class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        matrix = [[float("inf")] * (n + 1) for i in range(m + 1)]
    
        for i in range(m + 1):
            matrix[i][n] = m - i
        for j in range(n + 1):
            matrix[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i+1][j+1]
                else:
                    matrix[i][j] = 1 + min(matrix[i+1][j+1], matrix[i+1][j], matrix[i][j+1])

        return matrix[0][0]        