조이스틱
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.



import string

def solution(name):
    answer = 0
    name_len = len(name)
    alphabet = string.ascii_uppercase #	ABCDEFGHIJKLMNOPQRSTUVWXYZ
    alphabet_reverse = alphabet[::-1] # ZYXWVUTSRQPONMLKJIHGFEDCBA
    min_move = name_len-1 # 정방향으로 진행했을 때 최소조작횟수

    next = 0
    for idx, c in enumerate(name):
        forward = alphabet.index(c)
        reverse = alphabet_reverse.index(c)+1
        answer += min(forward, reverse) # 알파벳 선택 최소 조작 횟수를 결과에 추가
        
        next = idx + 1
        while next < name_len and name[next] == 'A': # 'A'가 아닌 문자를 만날때까지 증가시킴
            next += 1

        min_move = min(min_move, idx + idx + name_len - next) # 현재까지 커서 최소조작횟수와, 현재 위치에서 커서를 반대방향으로 옮기는 조작횟수를 비교하여 최소값을 갱신
    
    answer += min_move # 커서 최소조작횟수를 결과에 추가
    return answer
