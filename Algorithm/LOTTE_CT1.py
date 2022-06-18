def solution(penter, pexit, pescape, data):
    answer = ''
    data_len = len(penter)
    datas = []
    answer += penter

    for i in range(0, len(data), data_len):
        datas.append(data[i:i+data_len])

    for d in datas:
        if d == penter or d == pexit or d == pescape:
            answer += pescape
        answer += d

    answer += pexit

    return answer
