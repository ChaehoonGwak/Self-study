카펫
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.



def solution(brown, yellow):
    divisor = [] # yellow 의 약수를 넣을 리스트 초기화
    total = brown+yellow # 모든 격자의 합
    
    for i in range(1, yellow):
        if yellow % i == 0: # 약수일 때
            if (yellow // i) == i: # 완전제곱수라면 2번 삽입
                divisor.append(i)
            divisor.append(yellow//i) # 리스트에 삽입
            
    divisor.append(1)

    if len(divisor) == 1: return [3,3] # yellow가 1일 경우
    
    half_len = len(divisor) // 2
    for d in zip(divisor[:half_len], divisor[:half_len-1:-1]): # 맨앞과 맨뒤에서 차례대로 zip
        # yellow를 만들 수 있는 조합의 수들에 2를 더하고 곱한 값이 total과 같으면 그 수가 가로, 세로 값임
        # yellow == (x-2) * (y-2)
        # total == x * y
        x = d[0]+2 
        y = d[1]+2
        if x * y == total:
            return [x,y]
