N, M= input().split()
answer = []

five_N = N.replace('6','5')
five_M = M.replace('6','5')

six_N = N.replace('5','6')
six_M = M.replace('5','6')

#print(five_N, five_M, six_N, six_M)

#print(max(six_N,N))
#print(max(six_M,M))

# answer.append(int(min(five_N, N)) + int(min(five_M,M)))
# answer.append(int(max(six_N, N)) + int(max(six_M,M)))

answer.append(int(five_N) + int(five_M))
answer.append(int(six_N) + int(six_M))

# print(answer) # 다시 돌릴거면 처음부터 돌려야함

for i in range(2):
  print(answer[i], end=' ')
