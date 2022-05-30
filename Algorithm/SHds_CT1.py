N, M = map(int, input().split())
graph = [[0]*100 for _ in range(100)]
block = [list(map(int, input().split())) for _ in range(N)]

for b in block:
  ld = b[0]
  ru = b[-1]
  for i in range(ld-1, ru):
    for j in range(ld-1, ru):
      graph[i][j] += 1

cnt= 0

for i in graph:
  for j in i:
    if j > M:
      cnt += 1
      
print(cnt)
