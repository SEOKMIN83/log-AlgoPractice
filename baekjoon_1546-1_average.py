# MY 풀이

n = int(input())
scores = list(map(int, input().split(" ")))

max_score = max(scores)
new_sum = 0

for score in scores:
    new_sum += int(score) / int(max_score) * 100

#print("{:.6f}".format(new_sum / n)) # 소수점 자릿수 제한
print(round(new_sum/n, 6))
# 소수점 자릿수가 6자리 이상이면 => 6자리까지만 출력 / 소수점 자릿수가 6자리 미만이면 => 6자리까지 말고 그 자릿수까지만 출력
