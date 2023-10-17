n = int(input())

cnt = 0

if n == 1 or n ==3: # 1 <= n 범위가 1부터 시작, n= 1, 3이면 2와5로 나눠줄 수 없다
  print(-1)

while n>=0 :
  if n%5 == 0: # n -= 2를 더 위에 넣었을 때 숫자가 1 더 적게 나옴
    print(n//5 + cnt) # /로만 나누면 4.0, 5.0이 됨
    break
  n -= 2
  cnt+=1