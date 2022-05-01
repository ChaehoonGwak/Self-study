from itertools import combinations

def solution(needs, r):
    max_products = 0
    robots = [i for i in range(len(needs[0]))]
    combs = list(combinations(robots, r))
    
    for comb in combs:
        temp = 0

        for need in needs:
            flag = True
            for idx, parts in enumerate(need):
                if parts == 1 and idx not in comb:
                    flag = False
                    break
            if flag:
                temp += 1

        max_products = max(max_products, temp)

    return max_products
