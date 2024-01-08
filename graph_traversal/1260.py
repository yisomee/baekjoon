from collections import deque

# DFS와 BFS_실버2
# 리팩토링 필요

a, b, c = map(int, input().split())
graph = [[] for i in range(a+1)]
d_visited = [0]*(a+1)
b_visited = [0]*(a+1)
d_list = []
b_list = []
for i in range(b):
    d, e = map(int, input().split())
    graph[d]+=[e]
    graph[e]+=[d]
    graph[d].sort()
    graph[e].sort()

def dfs(x) :
    d_visited[x] = 1
    d_list.append(x)
    for i in graph[x]:
        if d_visited[i] == 0:
            dfs(i)
            
def bfs(z) :
    queue = deque([z])
    # b_list.append(z)
    b_visited[z] = 1
    while queue:
        v = queue.popleft()
        b_list.append(v)
        for i in graph[v]:
            if b_visited[i] == 0:
                queue.append(i)
                # b_list.append(i)
                b_visited[i] = 1
            
dfs(c)
bfs(c)
print(*d_list)
print(*b_list)