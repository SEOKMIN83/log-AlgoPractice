# 입력 ; M & N
import math

M, N = map(int, input().split())

# 숫자 리스트
num_list = [i for i in range(N+1)]
num_list[1] = 0

for i in range(2, int(math.sqrt(N)) + 1):   # 제곱근까지만!
    # 첫 번째 시도보다 더 깔끔하게 가능!
    if num_list[i] == 0:
        continue
    for j in range(i+i, N+1, i):
        num_list[j] = 0

# 출력
for i in range(M, N+1):
    if num_list[i] != 0:
        print(num_list[i])
