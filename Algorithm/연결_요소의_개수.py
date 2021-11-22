11724

문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.



import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 제한을 확대해야 함


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)
visited[0] = True
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

while False in visited: # 모든 노드들을 방문하여 연결 요소 갯수를 구함
    i = visited.index(False)
    dfs(graph, i, visited)
    answer += 1
    
print(answer)
