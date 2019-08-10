import sys
import collections

q = collections.deque()
arrow = [[0,1], [1,0], [0,-1], [-1,0]]
def bfs(x, y, number):
    q.append((x,y))
    while(len(q) != 0):
        t_x, t_y = q.popleft()

        for i in range(len(arrow)):
            c_x = t_x + arrow[i][0]
            c_y = t_y + arrow[i][1]

            if(c_x < len(matrix) and c_x >= 0 and c_y < len(matrix[0]) and c_y >= 0):
                if(matrix[c_x][c_y] == 1):
                    q.append((c_x, c_y))
                    matrix[c_x][c_y] = number

y = int(input())
matrix = [ list(map(int, sys.stdin.readline().strip())) for i in range(y)]
visited = [[0] * len(matrix[0]) for i in range(len(matrix))]
number = 2
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j] == 1 and visited[i][j] == 0):
            matrix[i][j] = number
            bfs(i, j, number)
            number += 1
"""for i in range(len(matrix)):
    print(matrix[i])"""
print(matrix)