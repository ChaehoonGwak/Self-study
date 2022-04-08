문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.



from collections import deque

def solution(progresses, speeds):
    answer = []
    job_days = deque()
    job_len = len(progresses)
    
    for i in range(job_len): # 작업 개발 일수를 계산하여 큐에 삽입
        job_days.append((99 - progresses[i]) // speeds[i] + 1)
        
    while(job_days):
        job_left = job_days.popleft() # 비교를 위해 첫 작업을 pop
        finish_cnt = 1 # pop했으므로 cnt는 1로 시작
        
        while(job_days and job_left >= job_days[0]): # pop한 원소보다 작은 작업을 만날때까지 pop하고 cnt 증가
            job_days.popleft()
            finish_cnt += 1
        
        answer.append(finish_cnt) # 배포 될때마다 배포된 작업의 개수를 삽입

    return answer
