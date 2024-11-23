from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

# 캠퍼스 정보
campus = []
start_x = start_y = -1

for i in range(N):
    row = list(input().rstrip())  # 각 행의 정보 리스트로 받기
    for j in range(M):
        if row[j] == 'I':  # 시작점
            start_x, start_y = i, j
    campus.append(row)

# BFS - 큐, 방문 처리 배열
queue = deque([(start_x, start_y)])
visited = [[False] * M for _ in range(N)]

people_count = 0

# BFS 탐색 방향 - 4
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited[start_x][start_y] = True  # 시작점은 방문

while queue:
    x, y = queue.popleft()

    # 4방향 탐색
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 캠퍼스 범위 내에서 벗어나지 않도록
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and campus[nx][ny] != 'X':  # 벽이 아니고, 방문하지 않은 곳
                visited[nx][ny] = True
                queue.append((nx, ny))

                # 사람이면 cnt
                if campus[nx][ny] == 'P':
                    people_count += 1

if people_count > 0:
    print(people_count)
else:
    print('TT')
