"""
입력
n(재료의 개수), m(갑옷이 완성되는 번호의 합), materials(재료들 리스트)

first_idx, second_idx = 0, n-1
answer = 0
재료들 리스트 '오름차순 정렬'

while first_idx < second_idx:
    two_sum = materials[first_idx] + materials[second_idx]
    만약 two_sum < m:
        first_idx += 1
    만약 two_sum == m:
        answer += 1
        first_idx += 1
        second_idx -= 1
    만약 two_sum > m:
        second_idx -= 1

answer 출력
"""
import sys

# 입력
input = sys.stdin.readline
n = int(input())
m = int(input())
materials = list(map(int, input().split()))

first_idx, second_idx = 0, n - 1
answer = 0

# 재료들 리스트 '오름차순 정렬'
materials.sort()

while first_idx < second_idx:
    two_sum = materials[first_idx] + materials[second_idx]
    if two_sum < m:
        first_idx += 1
    if two_sum == m:
        answer += 1
        first_idx += 1
        second_idx -= 1
    if two_sum > m:
        second_idx -= 1

# 출력
print(answer)
