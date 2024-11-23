from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부 2D 리스트
visited = [[0] * n for _ in range(n)]

def bfs(start):
    # BFS 탐색큐
    queue = deque([start])
    check = [0] * n  # 현재 노드 방문 여부 확인

    while queue:
        current = queue.popleft()

        # 모든 노드에 대해 연결되어 있는지
        for i in range(n):
            if check[i] == 0 and graph[current][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[start][i] = 1  
# 각 노드에서 BFS를 실행하여 연결된 노드들 탐색
for i in range(n):
    bfs(i)

for row in visited:
    print(*row)
