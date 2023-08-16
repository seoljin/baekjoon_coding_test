t = int(input()) # 테스트케이스의 수
answer = []

home = [[0]*15 for _ in range(15)]
#print(home)

home[0] = [i for i in range(15)]
#print(home)

for i in range(1,15):
  home[i][1]=1
#print(home)

for i in range (1,15):
    for j in range(2,15):
        home[i][j] = home[i][j-1] + home[i-1][j]
        
for i in range(t):
    k,n = [int(input()) for _ in range(2)] # 층,호
    answer.append(home[k][n])
    
for i in range(t):
  print(answer[i], end='\n')