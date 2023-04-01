# MY 풀이

"""
n(숫자 개수), m(divisor) 입력 받기
num_list(n개의 숫자들) 입력 받기 => [0] + 입력 받은 리스트

combination(조합 nC2 리스트) 선언
combination = [0] * m

answer(연속 부분 합이 m으로 나누어떨어지는 구간의 개수)
answer = 0

divided_sum_list(구간합 + m에 의한 나머지 리스트) 선언 => [0] * (n+1)
구간합 구하기 & 그 자체로 m으로 나눠지는 수를 통한 answer 구하기 & combination 구하기
for i in 1~n :
    divided_sum_list[i] = (sum_list[i-1] + num_list[i]) % m
    if divided_sum_list[i] == 0:
        answer += 1
    combination[divided_sum_list[i]] += 1

combination을 통한 answer 구하기
for i in range(m):
    answer += (combination[i] * (combination[i] - 1)) / 2

answer 출력
"""

import sys

input = sys.stdin.readline

# n(숫자 개수), m(divisor) 입력 받기
n, m = map(int, input().split())
num_list = [0] + list(map(int, input().split()))

# combination(조합 nC2 리스트) 선언
combination = [0] * m

# answer(연속 부분 합이 m으로 나누어 떨어지는 구간의 개수)
answer = 0

# divided_sum_list(구간합 + m에 의한 나머지 리스트) 선언
divided_sum_list = [0] * (n+1)
    # 책에서는 합배열인 sum_list는 합배열대로 구하고, 합배열에서의 '나머지' 값은 remainder라는 이름의 변수에 저장하는 식으로, 좀 더 값을 명료하게 알 수 있게 함

# 구간합 구하기 & 그 자체로 m으로 나눠지는 수를 통한 answer 구하기 & combination 구하기
for i in range(1, n +1) :
    divided_sum_list[i] = (divided_sum_list[i-1] + num_list[i]) % m
    if divided_sum_list[i] == 0:
        answer += 1
    combination[divided_sum_list[i]] += 1

# combination을 통한 answer 구하기
for i in range(m):
    answer += (combination[i] * (combination[i] - 1)) // 2

# answer 출력
print(answer)
