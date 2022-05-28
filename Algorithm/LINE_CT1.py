from collections import defaultdict

def solution(logs):
    answer = []
    problem = defaultdict(int)
    user = set()

    logs = list(set(logs))

    for log in logs:
        l = log.split(' ')
        user.add(l[0])
        problem[l[1]] += 1
    
    avg = len(user) / 2
    
    for p in problem:
        if problem[p] >= avg:
            answer.append(p) 

    answer.sort()

    return answer
