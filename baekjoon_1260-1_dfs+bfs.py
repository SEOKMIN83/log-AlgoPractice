# 입력 - Vertex 개수, Edge 개수, 시작 vertex
N, M, Start = map(int, input().split())

# 입력 - 그래프(인접 리스트)
A = [[] for i in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
for i in range(N + 1):
    A[i].sort()  # 정렬 (오름차순)

#  방문 체크 리스트
visited = [False] * (N + 1)


# DFS
def DFS(V):
    print(V, end=' ')  # 탐색 vertex 기록
    visited[V] = True
    for v in A[V]:
        if not visited[v]:
            DFS(v)  # 스택 (재귀함수)


DFS(Start)
print()

visited = [False] * (N + 1)  # 방문 체크 리스트의 초기화

# BFS

from collections import deque  # 큐


# BFS
def BFS(V):
    dq = deque()
    dq.append(V)
    visited[V] = True
    while dq:
        now_Vertex = dq.popleft()
        print(now_Vertex, end=' ')
        for v in A[now_Vertex]:
            if not visited[v]:
                visited[v] = True
                dq.append(v)


BFS(Start)

visited = [False] * (N + 1)
