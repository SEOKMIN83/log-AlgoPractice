"""
n(표의 크기, 1024 이하), m(합을 구해야 하는 횟수, 10만 이하)
table_data (원본 표 ; (n+1)*(n+1) ; 원래 크기보다 1 더 큰 사이즈로 만들어줌 ; 0으로 초기화)
table_sum (구간 합 테이블 ; (n+1)*(n+1))

n과 m 입력 받기

for 1~n까지:
    원본 표 table_data 채우기

for 1~n까지:
    for 1~n까지:
        (1,1) ~ (x, y)까지의 구간 합 구하기
        공식: table_sum[x, y] = table_data[x, y] + table_sum[x, y-1] + table_sum[x-1, y] - table_sum[x-1, y-1]

for m만큼 반복:
    x1, y1, x2, y2 입력 받기
    답 = table_sum[x2, y2] - table_sum[x2, y1-1] - table_sum[x1-1, y2] + table_sum[x1-1, y1-1]
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
table_data = [[0] * (n+1) for _ in range(n+1)]
table_sum = [[0] * (n+1) for _ in range(n+1)]
# 참고-1) 책에서는 table_data = [[0] * (n+1)] 로 초기화함. 즉, (n+1)*(n+1) 테이블의 맨 첫 행만 일단 설정. 그 이유는... (GO '참고-2')

# 원본 표 table_data 채우기
for i in range(1, n +1):
    row_data = [0] + list(map(int, input().split()))    # list끼리의 '+' 연산
    table_data[i] = row_data
# 참고-2) 책에서는
# for i in range(n):
#     row_data = [0] + [int(x) for x in input().split()]
#     table_data.append(row_data)
# 이렇게 맨 첫 행 이후의 행들은 append를 하는 방식으로 원본 테이블 table_data를 입력 받음
# 나는 일단 (n+1)*(n+1)으로 선언하고, 각 행을 '갈아끼우는' 식으로 원본 테이블 table_data를 입력 받았음

for x in range(1, n +1):
    for y in range(1, n +1):
        table_sum[x][y] = table_data[x][y] + table_sum[x][y - 1] + table_sum[x - 1][y] - table_sum[x - 1][y - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = table_sum[x2][y2] - table_sum[x2][y1-1] - table_sum[x1-1][y2] + table_sum[x1-1][y1-1]
    print(answer)
