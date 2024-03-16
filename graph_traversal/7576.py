# 토마토_골드5
from collections import deque

m,n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
queue = deque()
day = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
                queue.append((i,j))

def bfs():
    while queue:
        global day
        x,y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < n and 0 <=ny < m and graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
                
                day = graph[nx][ny]
            
bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            day = -1
            break

if day == 0 or day == -1:
    print(day)
else:
    print(day-1)