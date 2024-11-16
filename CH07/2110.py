# n: 집의 개수, c: 공유기 개수
n, c = map(int, input().split())

# 집들의 좌표를 저장할 리스트
array = []
for i in range(n):
    array.append(int(input()))

# 집들을 오름차순으로 정렬
array.sort()

# 이진 탐색 함수 정의
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2  # 중간 거리 계산
        current = array[0]  # 첫 번째 집에 공유기 설치
        count = 1  # 첫 번째 집에 공유기 설치 카운트

        # 나머지 집들에서 조건을 만족하는 경우에만 공유기 설치
        for i in range(1, len(array)):
            if array[i] >= current + mid:  # 공유기 설치 조건
                count += 1  # 공유기 설치
                current = array[i]  # 최근 설치한 집 갱신

        # 공유기 수가 c 이상이면 거리를 늘려서 다시 탐색
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1  # 설치 불가 시 거리를 줄임

# 탐색할 거리의 범위 설정 (최소 1, 최대 집들 간의 최대 거리)
start = 1
end = array[-1] - array[0]
answer = 0  # 최적의 거리

# 이진 탐색 실행
binary_search(array, start, end)

# 최종 결과 출력
print(answer)
