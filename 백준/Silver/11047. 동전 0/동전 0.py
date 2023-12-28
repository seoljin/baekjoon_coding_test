N, K = map(int,input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
    
#arr[::-1]

answer = 0
for coin in arr[::-1]:
    if coin <= K:
        answer += K // coin
        K = K % coin
print(answer)