문제 설명
입금 내역만 표시되는 통장을 개설했습니다. 이 통장은 입금과 출금 모두 가능하지만, 거래 내역에는 입금 내용만 표시됩니다. 이 통장에 입금 또는 출금을 할 때는 다음과 같은 규칙을 따릅니다.

입금한 금액은 입금 순서대로 통장에 표시됩니다.
입금 내용마다 나누어서 표시됩니다.
출금할 때는 가장 마지막에 입금한 내용부터 하나씩 삭제하며 출금액을 맞춥니다.
출금액을 맞춘 후 남은 액수를(1원 이상 남은 경우) 가장 마지막에 입금한 내역으로 추가합니다.
예를 들어 입출금 내용이 다음과 같은 경우

[500원 입금, 1000원 입금, 300원 출금, 200원 입금, 400원 출금, 100원 입금, 100원 출금]

통장에 기록되는 내용은 다음과 같습니다.

입출금 내용	표시 내역	설명
500원 입금	[500]	500원 입금한 내용이 추가됩니다.
1000원 입금	[500, 1000]	1000원 입금한 내용이 추가됩니다.
300원 출금	[500, 700]	가장 마지막에 입금한 내역부터 순서대로 제거하며 300원을 출금합니다. 남은 금액 700원을 가장 마지막에 입금한 내역으로 추가합니다.
200원 입금	[500, 700, 200]	200원 입금한 내용이 추가됩니다.
400원 출금	[500, 500]	가장 마지막에 입금한 내역부터 순서대로 제거하며 400원을 출금합니다. 남은 금액 500원을 가장 마지막에 입금한 내역으로 추가합니다.
100원 입금	[500, 500, 100]	100원 입금한 내용이 추가됩니다.
100원 출금	[500, 500]	가장 마지막에 입금한 내역부터 순서대로 제거하며 100원을 출금합니다. 남은 금액이 없으므로 아무 내역도 추가하지 않습니다.
따라서 입금 내용만 기록하는 통장에는 [500원 입금, 500원 입금]이 표시됩니다.

입출금한 내용이 담긴 배열 deposit이 매개변수로 주어질 때, 모든 내용을 처리후 통장에 표시되는 내용을 return 하도록 solution 함수를 완성해주세요.

제한사항
deposit의 길이는 1 이상 1,000 이하입니다.
deposit의 원소는 -1,000,000 이상 1,000,000 이하인 0이 아닌 정수입니다.
양수는 입금 내용, 음수는 출금 내용을 나타냅니다.
통장에 입금된 금액보다 큰 금액을 출금하는 경우는 없습니다.
정답으로 return 하는 배열 길이가 1 이상인 경우만 입력으로 주어집니다.



def solution(deposit):
    answer = []

    for d in deposit:
        if d > 0:
            answer.append(d)
        else:
            minus_d = abs(d)
            
            if answer[-1] > minus_d:
                answer[-1] = answer[-1] - minus_d

            elif answer[-1] < minus_d:
                while answer[-1] < minus_d:
                    minus_d -= answer[-1]
                    answer.pop()
                answer[-1] = answer[-1] - minus_d
                
            elif answer[-1] == minus_d:
                answer.pop()

    return answer