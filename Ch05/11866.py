import sys

# 입력 받기
n, k = map(int, sys.stdin.readline().split())

# 요세푸스 순열 생성
idx = 0
queue = [i for i in range(1, n + 1)]  # 1부터 n까지의 숫자를 큐에 저장
res = []

while queue:
    idx += k - 1  # k-1만큼 인덱스 이동
    if idx >= len(queue):  # 인덱스가 범위를 넘어갈 경우
        idx %= len(queue)  # 나머지로 인덱스 조정
    res.append(str(queue.pop(idx)))  # k번째 수 제거하고 결과에 추가

# 결과 출력
print("<", ", ".join(res), ">", sep="")
