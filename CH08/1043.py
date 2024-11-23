import sys
input = sys.stdin.readline

n, m = map(int, input().split())
truth_knowers = set(input().split()[1:])  # 진실을 아는 사람들
parties = [set(input().split()[1:]) for _ in range(m)]  # 파티 참석자들

# 진실을 아는 사람이 포함된 파티에 참석지 추가
for _ in range(m):
    for party in parties:
        if party & truth_knowers:
            truth_knowers |= party

# 진실을 아는 사람이 포함되지 않은 수
safe_party_count = sum(1 for party in parties if not party & truth_knowers)
print(safe_party_count)
