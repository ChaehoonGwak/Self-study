def dfs(number, target):
  global answer
  if number > target:
    return
  elif number == target:
    answer += 1
    return
  
  dfs(number+1, target)
  dfs(number+2, target)
  dfs(number+3, target)
  
M = int(input())
for _ in range(M):
    target = int(input())
    global answer
    answer = 0
    dfs(0, target)
    print(answer)
