import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# deque 탐색
queue = deque([[n]])  # 시작값
result = []

while queue:
    sequence = queue.popleft()  # 큐에서 첫 번째 시퀀스를 꺼냄
    current = sequence[0]  # 현재 숫자

    if current == 1:  # 1 도달 시 종료
        result = sequence
        break

    # x가 3으로 나누어지면 큐에 추가
    if current % 3 == 0:
        queue.append([current // 3] + sequence)

    # x가 2로 나누어지면 큐에 추가
    if current % 2 == 0:
        queue.append([current // 2] + sequence)
    
    # x에서 1을 빼고 큐에 추가
    queue.append([current - 1] + sequence)


print(len(result) - 1)  # 최단 경로의 길
print(*result[::-1])  # 경로(뒤집어서)
