문제 설명
세 명의 사람들이 가위바위보를 진행합니다. 매 판마다 승자는 다음 규칙에 따라 점수를 얻습니다.

승자가 1명인 경우: 해당 승자는 2점을 얻습니다.
승자가 2명인 경우:
두 승자의 누적 점수가 같은 경우: 각 승자는 1점씩 얻습니다.
두 승자의 누적 점수가 다른 경우: 둘 중 누적 점수가 낮은 승자가 2점을 얻습니다.
승자가 없는 경우(모두 같은 수를 내거나, 모두 다른 수를 냈을 경우): 아무도 점수를 얻지 않습니다.
3인 가위바위보 결과를 나타내는 문자열 배열 rsp3가 매개변수로 주어집니다. 
rsp3의 순서대로 가위바위보를 진행한 뒤 각 사람의 누적 점수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ rsp3의 길이 ≤ 100,000
rsp3의 각 문자열의 길이 = 3
rsp3[i]는 i+1번째 판의 결과를 의미합니다.
rsp3[i]는 1번째 사람이 낸 수 + 2번째 사람이 낸 수 + 3번째 사람이 낸 수로 이루어져 있습니다.
rsp3의 모든 문자열은 'R', 'S', 'P'로 이루어져 있습니다.
'R'은 바위(Rock), 'S'는 가위(Scissor), 'P'는 보(Paper)를 의미합니다.
예를 들어, rsp3[i] = "PPS" 일 경우, 1번째 사람과 2번째 사람은 보를 내고 3번째 사람은 가위를 냈습니다. 따라서, 3번째 사람이 해당 판의 유일한 승자이고 승점 2점을 얻습니다.



from collections import Counter

def solution(rsp3):
    answer = [0, 0, 0]
    
    for rsp in rsp3:
        cnt = Counter(rsp)
        
        if len(cnt) == 1 or len(cnt) == 3:
            continue
        else:
            temp = []
            index = -1
            if 'R' in rsp and 'S' in rsp:
                while True:
                    index = rsp.find('R', index+1)
                    if index != -1:
                        temp.append(index)
                    if index == -1:
                        break

                if cnt['R'] == 2:
                    if answer[temp[0]] == answer[temp[1]]:
                        answer[temp[0]] += 1
                        answer[temp[1]] += 1
                    elif answer[temp[0]] > answer[temp[1]]:
                        answer[temp[1]] += 2
                    elif answer[temp[0]] < answer[temp[1]]:
                        answer[temp[0]] += 2
                
                else:
                    answer[temp[0]] += 2

                
            elif 'S' in rsp and 'P' in rsp:
                while True:
                    index = rsp.find('S', index+1)
                    if index != -1:
                        temp.append(index)
                    if index == -1:
                        break

                if cnt['S'] == 2:
                    if answer[temp[0]] == answer[temp[1]]:
                        answer[temp[0]] += 1
                        answer[temp[1]] += 1
                    elif answer[temp[0]] > answer[temp[1]]:
                        answer[temp[1]] += 2
                    elif answer[temp[0]] < answer[temp[1]]:
                        answer[temp[0]] += 2

                else:
                    answer[temp[0]] += 2

                
            elif 'P' in rsp and 'R' in rsp:
                while True:
                    index = rsp.find('P', index+1)
                    if index != -1:
                        temp.append(index)
                    if index == -1:
                        break

                if cnt['P'] == 2:
                    if answer[temp[0]] == answer[temp[1]]:
                        answer[temp[0]] += 1
                        answer[temp[1]] += 1
                    elif answer[temp[0]] > answer[temp[1]]:
                        answer[temp[1]] += 2
                    elif answer[temp[0]] < answer[temp[1]]:
                        answer[temp[0]] += 2

                else:
                    answer[temp[0]] += 2
                
    return answer
