문제 설명
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 2 이상 100 이하인 자연수입니다.
wires는 길이가 n-1인 정수형 2차원 배열입니다.
wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
1 ≤ v1 < v2 ≤ n 입니다.
전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.



from collections import deque

def bfs(graph, v, visited):
    q = deque([v])
    result = 1 # 이어진 노드 개수를 리턴할 변수 초기화
    visited[v] = True
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                result += 1
                visited[i] = True
                
    return result

def solution(n, wires):
    answer = 101 # n은 100이하 자연수
    graph = [[] for _ in range(n+1)] # 
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    # 현재 전선의 시작점으로 bfs 탐색, 이어진 곳을 visit 처리함으로 끊음
    for start, not_visit in wires:
        visited = [False] * (n+1) # 방문 배열 초기화
        visited[not_visit] = True # 끊어짐 처리
        result = bfs(graph, start, visited) # start와 이어진 노드 탐색하여 연결된 갯수 리턴받음
        answer = min(answer, abs(result - (n - result))) # 가장 차이가 나지 않는 개수를 갱신
    
    return answer
