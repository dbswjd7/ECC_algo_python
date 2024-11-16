import sys

num_first_list = int(sys.stdin.readline().strip())  # 첫 번째 리스트 크기
first_list = list(map(int, sys.stdin.readline().strip().split()))  # 첫 번째 리스트 원소

num_second_list = int(sys.stdin.readline().strip())  # 두 번째 리스트 크기
second_list = list(map(int, sys.stdin.readline().strip().split()))  # 두 번째 리스트 원소

# first_list 각 원소 빈도를 저장하는 딕셔너리
frequency_dict = {}

# 빈도수 계산
for num in first_list:
    if num in frequency_dict:
        frequency_dict[num] += 1  # 이미 존재: 빈도수 증가
    else:
        frequency_dict[num] = 1  # 처음 등장: 빈도수 1

# second_list의 각 원소에 대해 first_list에서의 빈도 출력
for target in second_list:
    if target in frequency_dict:
        print(frequency_dict[target], end=' ')  # first_list에 있으면 해당 빈도 출력
    else:
        print(0, end=' ')  # first_list에 없으면 0 출력
