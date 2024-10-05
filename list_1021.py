# 양방향으로 회전하므로 deque 사용
from collections import deque
import sys

# 입력 받기 위해 sys.stdin.readline 사용
keyboard = sys.stdin.readline

# 첫째 줄 입력받고 N(처음 포함 수), loc(뽑아내려고 하는 원소 위치)로 split
N, loc = map(int, keyboard().split())

# deque 생성 1 - N
dq = deque()
for i in range(N):
    dq.append(i+1)


output = list(map(int, keyboard().split())) # 뽑아낼 output
## 반복문
## while 첫 원소만 남을 때까지 회전(왼 or 오) 
cnt = 0
for i in output:
    while 1:
        # 0번째 index와 같으면 popleft, break
        if i ==dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(i) > len(dq) //2:
                dq.appendleft(dq.pop())
                cnt+=1
            else:
                dq.append(dq.popleft())
                cnt+=1

print(cnt)