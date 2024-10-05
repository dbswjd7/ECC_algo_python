# 양방향으로 회전하므로 deque 사용
from collections import deque
import sys, random 
keyboard = sys.stdin.readline

n = keyboard()
N = int(n)


# deque 생성 -N ~ N 사이의 수가 랜덤으로 
dq = deque()
for i in range(N):
    num = random.randrange(-N, N)
    dq.append(num)

#print(dq)

# 풍선 터뜨리기
idx = 0
ans=[]
while dq:
    idx = dq.popleft()
    ans.append(idx+1)
    
    if idx >0:
        dq.rotate(-(idx-1))
    else:
        dq.rotate(-idx)

print(ans)

    
