문제 설명
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 
권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 
심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
선수의 수는 1명 이상 100명 이하입니다.
경기 결과는 1개 이상 4,500개 이하입니다.
results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.



def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)] # 경기결과 그래프 초기화

    for result in results: # results를 경기결과 그래프에 반영
        winner = result[0]-1; loser = result[1]-1
        graph[winner][loser] = 1; graph[loser][winner] = -1
    
    # 플로이드-워셜 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or graph[i][j] in [1,-1]: # 자기 자신이거나 이미 처리했다면 패스
                    continue
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = graph[k][i] = graph[j][k] = -1
                    # print(i,j,k, *graph,sep="\n")

    for r in graph:
        if r.count(0) == 1: # 0이 하나라면 순위를 알 수 있으므로 answer ++
            answer += 1
            
    return answer
