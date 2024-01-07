# 바이러스_실버3

a = int(input())
b = int(input())

graph = [[] for i in range(a+1)]
visited = [0] * (a+1)
for i in range(b):
    c,d = map(int, input().split())
    graph[c] += [d]
    graph[d] += [c]

def dfs(i) :
    visited[i] = 1
    for k in graph[i] :
        if visited[k] == 0:
            dfs(k)   
dfs(1)
print(visited.count(1)-1)