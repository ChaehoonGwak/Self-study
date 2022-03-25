문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.



def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    
    for idx1, element in enumerate(zip(arr1, arr2)):
        for idx2 in range(len(element[0])):
            temp = 0
            for idx3 in range(len(element)):
                temp += element[idx3][idx2]
            answer[idx1][idx2] = temp
        
    return answer
  
  
# 행렬은 numpy를 쓰면 쉽게 연산 가능
# import numpy as np

# def solution(arr1, arr2):
#     return (np.array(arr1) + np.array(arr2)).tolist()
