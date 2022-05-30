un = list(map(int, input().split()))

vn = 0
for i in un:
  vn += i*i
  
print(vn%10)
