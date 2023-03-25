# MY 풀이

N = int(input())
num_string = input()    # 일단 int 자체가 아닌 string으로 받았었는데, 이러면 int로의 형 변환을 쓸데없이 2번 해줘야 함

sum_result = 0

for i in range(N):  # 반복 횟수를 N에 의존하면, 만약 N != len(num_string)으로 입력값을 잘못 입력했을 때 에러 날 가능성 有
    sum_result += int(num_string[i])

print(sum_result)
