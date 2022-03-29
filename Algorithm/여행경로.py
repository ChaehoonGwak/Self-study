문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.



from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)
    
    for ticket in tickets: # tickets를 딕셔너리에 초기화
        routes[ticket[0]].append(ticket[1])
    for key in routes: # 알파벳 순서가 앞서는 경로로 return 해야 하므로 values sort
        routes[key].sort(reverse=True)
    
    stack = ["ICN"] # "ICN" 공항에서 출발
    while stack:
        temp = stack[-1] # stack의 top
        
        if not routes[temp]: # 경로가 없다면 stack의 top을 answer에 추가
            answer.append(stack.pop())
        else: # 경로가 있다면 stack에 추가
            stack.append(routes[temp].pop())
        
    answer.reverse() # stack의 top은 결과의 뒤부터 탐색한 것이므로 answer 뒤집어 줌
    
    return answer
