def solution(r, c):
    answer = [[]]
    graph = [[0]*c for _ in range(r)]
    nc = c-1
    nr = 0
    cnt = 1
    f = False

    # print(*graph, sep='\n')

    while True:
        while nc != -1 or graph[nr][nc-1] == 0:
            if graph[nr][nc] != 0:
                if cnt > r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nc -= 1
            cnt+=1

        nc += 1
        nr += 1
        if f: break

        while nr != r or graph[nr-1][nc] == 0:
            if graph[nr][nc] != 0:
                if cnt > r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nr += 1
            cnt += 1

        if f: break
        nc += 1
        nr -= 1

        while nc != c or graph[nr][nc-1] == 0:
            if graph[nr][nc] != 0:
                if cnt > r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nc += 1
            cnt += 1

        if f: break
        nr -= 1
        nc -= 1

        while nc != -1 or graph[nr][nc-1] == 0:
            if graph[nr][nc] != 0:
                if cnt > r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nc -= 1
            cnt+=1

        nc += 1
        nr -= 1
        if f: break

        while nr != r or graph[nr-1][nc] == 0:
            if graph[nr][nc] != 0:
                if cnt >= r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nr -= 1
            cnt += 1

        nc += 1
        nr += 1
        if f: break

        while nc != c or graph[nr][nc-1] == 0:
            if graph[nr][nc] != 0:
                if cnt >= r*c:
                    f = True
                break
            graph[nr][nc] = cnt
            nc += 1
            cnt += 1

        nr += 1
        nc -= 1
        if f: break

    # print(*graph, sep='\n')

    answer = [i for i in graph]

    return answer
