# 모범 답안 참고

n = int(input())
scores = list(map(int, input().split(" ")))

max_score = max(scores)
sum = sum(scores)   # sum() 함수 => 바로 리스트의 총합 구해버릴 수 있음

print(round(sum / max_score * 100 / n, 6))
