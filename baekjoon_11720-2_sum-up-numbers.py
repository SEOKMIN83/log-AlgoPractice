# 모범 답안 참고

n = input()
numbers = list(input())  # 리스트 안의 숫자들을 한 자리씩 나누어 받음

sum = 0

for i in numbers:   # 굳이 index로 '간접' 접근할 필요 없이, 곧바로 원소들에 '직접' 접근
    sum += int(i)

print(sum)
