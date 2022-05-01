from collections import Counter

def solution(scores):
    answer = 0
    score_board = {'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0}

    for score in scores:
        counter = Counter(score)
        if counter['F'] >= 2:
            continue
        elif counter['A'] >= 2:
            answer += 1
            continue
        else:
            sum_score = 0
            sort_counter = sorted(counter.keys())
            counter[sort_counter[0]] -= 1
            counter[sort_counter[-1]] -= 1
            len_score = sum(counter.values())

            for c in counter:
                sum_score += counter[c] * score_board[c]

            if sum_score / len_score >= 3:
                answer += 1


    return answer
