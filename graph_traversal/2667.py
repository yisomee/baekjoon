# 단지 번호 붙이기_실버1
from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
result = 0
cnt = 0
total = []

def dfs(x,y):
    if x >= n or x < 0 or y >= n or y < 0:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        global cnt
        cnt += 1
        
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            result += 1
            total.append(cnt)
            cnt = 0
            
total.sort()
print(result)
for i in range(len(total)):
    print(total[i])
    