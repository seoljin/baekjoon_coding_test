n = int(input()) # 전체 사람의 수
body=[] # 키와 몸무게 리스트
answer= []


for i in range(n): # 키와 몸무게 입력
    x, y = map(int, input().split())
    body.append((x,y))

# print(body) -> 리스트가 잘 들어갔는지 확인용
# body[1] -> (50, 170)
# body[1][0] -> 50

for i in range(len(body)):
    cnt = 1     # 등수
    for j in range(len(body)):
        if body[i][0]<body[j][0] and body[i][1]<body[j][1]: # 비교
            cnt+=1
    answer.append(cnt) # 등수 리스트

# print(answer) 등수 확인용

for i in range(len(answer)):
  print(answer[i], end=' ')