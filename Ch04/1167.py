import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) 

# Graph
graph = [[] for _ in range(n+1)]
for _ in range(n):
    tree = list(map(int, input().split()))
    for i in range(1, len(tree)//2):
        graph[tree[0]].append((tree[2*i-1], tree[2*i]))



visited = [-1] * (n+1)
visited[1] = 0  



# DFS로 풀이
def DFS(x, distance):
    for i, w in graph[x]:
        # 아직 방문ㅌ: 현재까지의 거리 + 해당 노드까지를 더함
        if visited[i] == -1:
            visited[i] = distance + w
            DFS(i, distance + w)
            
DFS(1, 0)
max_distance = max(visited) 
max_node = visited.index(max_distance)


# max_node에서 시ekt
visited = [-1] * (n+1)
visited[max_node] = 0 
DFS(max_node, 0)

print(max(visited))