T = int(input())

prime = [True] * (1299709 + 1)
prime[0], prime[1] = False, False
for num in range(2, 1299709 + 1):
    if not prime[num]:
        continue
    for multiple in range(num * num, 1299709 + 1, num):
        prime[multiple] = False


for _ in range(T):
    N = int(input())

    if prime[N]:
        print(0)
    else:
        left = N  # 왼쪽으로 이동할
        right = N  # 오른쪽으로 이동할 
        count = 1  # 초기 N 포함 개수

        # 왼쪽으로 이동
        while not prime[left]:
            left -= 1
            count += 1  # 지나간 비소수

        # 오른쪽으로 이동
        while not prime[right]:
            right += 1
            count += 1  

        print(count + 1) 
