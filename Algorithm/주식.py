11501

문제
홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

주식 하나를 산다.
원하는 만큼 가지고 있는 주식을 판다.
아무것도 안한다.
홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 
따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 
그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.

입력
입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다. 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고, 
둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

출력
각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.



T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    answer = 0
    max_price = stock[-1] # 맨 마지막 날을 max로 설정
    
    for i in range(N-2, -1, -1):
        if stock[i] > max_price: # 더 큰 max 값이 나온다면 max 갱신
            max_price = stock[i]
        else: # i번째 가격이 최대가 아니라면 현재 max값에 주식 판매 
            answer += max_price - stock[i]
        
    print(answer)
    
    
    
# 시간초과

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     stock = list(map(int, input().split()))

#     answer = 0
    
#     for i in range(len(stock)-1): # 마지막 날은 판매만 하므로 len-1
#         profit = 0
        
#         for j in range(i+1, len(stock)): # i+1 부터 끝까지 탐색하여 최대로 팔수 있는 값을 찾는다
#             if stock[i] < stock[j]:
#                 profit = max(profit, stock[j] - stock[i]) # 현재 최댓값과 비교하여 갱신
        
#         if profit != 0:
#             answer += profit # 반복문이 끝나면 최대 수익을 볼 수 있는 값이므로 수익을 결과에 더함
            
#     print(answer)

