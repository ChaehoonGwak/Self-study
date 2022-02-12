문제 설명
엘보니아의 왕은 width미터 * length미터 넓이의 궁전에서 살고 있다. 
그는 신하들을 진흙 위에 살고 있게 하였기 때문에 인기 있는 왕은 아니었다. 
그는 방문자들이 그를 접견하기 위해 오래 걷게 만들고 싶어서 궁전을 나누고 싶어했다. 
왕의 보안 고문은 나선형으로 나누자고 제안했다. 
방문자는 남서쪽 모서리에서 입궁하여 동쪽으로 걷는다. 
방문자 앞에 벽이 나타나면 왼쪽으로 방향을 바꾼다. 
나선형 복도의 너비는 1미터이다.

아래 다이어그램은 나선형 길의 한 예제이다:
방문객은 a (남서쪽 모서리)에서 출발하여 알파벳 순서대로 x (왕좌)까지 이동한다.
nmlkji
oxwvuh
pqrstg
abcdef

왕은 궁전의 길을 새로 만들기 전에 그의 왕좌를 먼저 정확한 위치로 옮기고 싶어하기 때문에 나선형의 길이 어디서 끝날지 알아야 한다. 왕좌의 좌표를 두개의 정수로 리턴하시오.

남서쪽 모서리는 (0, 0)이고 남동쪽 모서리는 (width - 1, 0), 그리고 북동쪽 모서리는 (width - 1, length - 1)이다.

참고 / 제약 사항
width와 length는 둘 다 최소값 1, 최대값 5000의 범위를 가진다.



class Solution:
    def solution(self, width, length):
        check=x=y=0
        end=width*length
        
        while True:
            x+=(width-1)
            check+=width
            if check==end:
                return [x,y]
                
            y+=(length-1)
            check+=(length-1)
            if check==end:
                return [x,y]
                
            x-=(width-1)
            check+=(width-1)
            if check==end:
                return [x,y]
        
            y-=(length-2)
            check+=(length-2)
            if check==end:
              return [x,y]
        
            x+=1
            width-=2
            length-=2
