from collections import deque
import sys

# input ->  deque로 변환
string_list = deque(input())
cursor = len(string_list)  # 커서를 문자열의 끝으로 초기화

for _ in range(int(input())):  
    command = list(sys.stdin.readline().split()) 

    if command[0] == 'P':  # 'P' : 문자 추가
        string_list.insert(cursor, command[1])  # 커서 위치에 문자 추가
        cursor += 1  # 커서 한 칸 오른쪽으로 이동

    elif command[0] == 'L':  # 'L' 명령어: 커서 왼쪽으로 이동
        if cursor > 0:  # 커서 0보다 크ㄹ때만 이동
            cursor -= 1

    elif command[0] == 'D':  # 'D' 명령어: 커서 오른쪽으로 이동
        if cursor < len(string_list):  # 커서가 문자열의 길이보다 작을 때만 이동
            cursor += 1

    elif command[0] == 'B':  # 'B' 명령어: 왼쪽 문자 삭제
        if cursor > 0:  # 커서가 0보다 클 때만 삭제
            string_list.remove(string_list[cursor - 1])  # 커서 왼쪽 문자 삭제

# 결과를 문자열로 변환하여 출력
print(''.join(string_list))
