ir = input()
stack = []
cnt = 0

for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")  # 열린 괄호 추가
    else:
        if ir[i - 1] == "(":
            stack.pop()  # 막대기 끝
            cnt += len(stack)  # 현재 스택의 길이만큼 카운트
        else:
            stack.pop()  # 막대기 끝
            cnt += 1  # 단일 막대기 카운트

print(cnt)