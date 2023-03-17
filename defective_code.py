# 배열의 주어진 범위의 합을 2로 나눈 몫 구하기
import random

testcase = int(input())
answer = 0
A = [0] * (100001)

for i in range(0, 10001):   # 오류_2) 반복문에서의 인덱스 번위 지정 오류 : 100001 != 10001
    A[i] = random.randrange(1, 100+1)

for t in range(1, testcase+1):
    start, end = map(int, input().split())  # 오류_1) 변수 초기화 오류 : 이전 테스트케이스의 answer 값이 그대로 유지되어있음

    for i in range(start, end+1):
        answer += A[i]

    print(str(testcase) + " " + str(answer/2))
    # 오류_3) 잘못된 변수 사용 오류 : testcase 변수가 아닌 t 변수를 사용했어야 함
    # 오류_4) 파이썬 자동 형 변환 유의 : / => float형으로  자동 변환함. int형 출력을 위해서는 '/'가 아닌 '//'을 사용했어야 함
