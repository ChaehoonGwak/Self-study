def solution(A):
    answer = 0
    
    for i in range(len(A)):
        if sum(A[:i+1]) == ((i+1)*(i+2))//2:
            answer += 1

    return answer
