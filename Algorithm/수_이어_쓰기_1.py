1748

문제
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

출력
첫째 줄에 새로운 수의 자릿수를 출력한다.



N = input()

N_len = len(N)
iN = int(N)
d = 10**(N_len-1)
answer = 0

# N이 120 이라면 r = 21, N이 220 이라면 r = 121
if N[0] == '1': # 맨 앞자리 수가 1이면 맨 앞자리 수 제외한 나머지 수+1 을 len과 곱함
    r = iN%d+1
else: # 1이 아니라면 맨 앞자리 수 -1을 d와 곱하고 맨 앞자리 수 제외한 나머지 수+1 을 더한 뒤 len과 곱함
    r = (iN // d - 1) * d + (iN % d + 1)
    
answer = r*N_len

for i in range(N_len-1,0,-1): # 나머지는 자릿수(ex 100의 자리면 3, 10의 자리면 2) * 9*10^(자릿수-1)를 하여 결과에 더함
    d = d//10
    answer += i*9*d
    
print(answer) # 결과 출력
