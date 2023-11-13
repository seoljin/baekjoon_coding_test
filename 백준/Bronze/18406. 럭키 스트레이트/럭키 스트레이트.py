N = input()
leng = len(N)//2        # len(N)/2로 하면 float로 나타남 ㅠㅠ
sum_left = 0
sum_right = 0

for i in range(leng):   # leng길이까지 N의 값들 더하기
  sum_left += int(N[i])

for j in range(leng,len(N)): # leng부터 끝까지 N의 값들 더하기
  sum_right += int(N[j])

if sum_left == sum_right:   # 같으면 LUCKY
  print('LUCKY')
else:                       # 다르면 READY
  print('READY')