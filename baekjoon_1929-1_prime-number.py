# 입력 ; M & N
import math

M, N = map(int, input().split())

# 숫자 리스트
num_list = [i for i in range(N+1)]
num_list[1] = 0

for i in range(2, int(math.sqrt(N)) + 1):
    inc = 2
    no_prime = i * inc
    while no_prime <= N:
        num_list[no_prime] = 0
        inc += 1
        no_prime = i * inc

# 출력
for i in range(M, N+1):
    if num_list[i] != 0:
        print(num_list[i])
