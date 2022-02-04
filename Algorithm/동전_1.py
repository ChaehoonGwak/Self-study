2293

문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.



n, k = map(int, input().split())
coins = [int(input()) for i in range(n)]

dp = [0 for i in range(k+1)]    # dp 초기화
dp[0] = 1   # dp 성립을 위한 기본값

# 해당 코인과 현재까지 사용된 코인을 사용하여 coin부터 k까지 돌면서 i를 만들 수 있는 경우의 수를 dp에 누적하여 더함.
for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]
           
print(dp[k])
