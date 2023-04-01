# 책 참고한 ver.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [0] + list(map(int, input().split()))

combination = [0] * m

answer = 0

# sum_list(구간합 리스트) 선언
sum_list = [0] * (n+1)
for i in range(1, n +1):
    sum_list[i] = sum_list[i-1] + num_list[i]

# remainder(= 구간합 % m) 구하기 & 그 자체로 m으로 나눠지는 수를 통한 answer 구하기 & combination 구하기
for i in range(1, n +1) :
    remainder = sum_list[i] % m
    if remainder == 0:
        answer += 1
    combination[remainder] += 1

# combination을 통한 answer 구하기
for i in range(m):
    answer += (combination[i] * (combination[i] - 1)) // 2

# answer 출력
print(answer)
