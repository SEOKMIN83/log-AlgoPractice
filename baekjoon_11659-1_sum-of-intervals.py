# MY 풀이
import sys

input = sys.stdin.readline  # 이 코드의 유무만으로 '시간초과'와 '맞았습니다'가 결정됨 ; 입력 속도 : 일반 input() <<<<< sys.stdin.readline()
N, Q = map(int, input().split())
list_original = list(map(int, input().split()))

list_sum = [0]
temp = 0

# 아래 풀이도 OK
# for i in range(N):
#     temp = list_sum[i] + list_original[i]
#     list_sum.append(temp)

for i in list_original:
    temp += i
    list_sum.append(temp)   # '합 배열' 만들기

for i in range(Q):
    start, end = map(int, input().split())
    print(list_sum[end] - list_sum[start-1])    # 합 배열에서 '구간 합' 구하기
