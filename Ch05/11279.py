import heapq
import sys

input = sys.stdin.readline  

n = int(input())  
max_heap = []  # 최대 힙 리스트

for _ in range(n):
    number = int(input()) 

    if number > 0:
        heapq.heappush(max_heap, -number)  # 양수 -> 음수 변환해 힙에 추가
    else:
        if max_heap:  # 최대 힙 비어있지 않은 경우
            print(-heapq.heappop(max_heap))  # 최대 값 꺼내고 음수로 변환 후 출력
        else:
            print(0)  # 힙이 비어있으면 0 출력
