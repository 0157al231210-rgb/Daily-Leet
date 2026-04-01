import collections
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
       
        height = len(mat)
        width = len(mat[0])
        q = collections.deque()

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            row,col = q.popleft()
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < height and
                    0 <= nc < width and
                    mat[nr][nc] == -1):

                    mat[nr][nc] = mat[row][col] + 1
                    q.append((nr,nc))

        return mat 