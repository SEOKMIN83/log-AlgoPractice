# 투 포인터

import sys

input = sys.stdin.readline

# 입력값 n
n = int(input())

# 변수들 초기화
start_idx, end_idx = 1, 1
sub_sum = start_idx
answer = 1

# 단일 while문
# 전진 like a 지렁이 (꿈틀꿈틀..)
while end_idx != n:
    if sub_sum == n:  # 정답
        answer += 1
        # print("정답:", start_idx, end_idx, sub_sum) # 디버깅
        end_idx += 1
        sub_sum += end_idx
    elif sub_sum > n:
        sub_sum -= start_idx
        start_idx += 1
    else:
        # print(start_idx, end_idx, sub_sum) # 디버깅
        end_idx += 1
        sub_sum += end_idx

print(answer)
