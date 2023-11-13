def num(n):               # 생성자인 / 셀프넘버가 아닌 숫자를 구하는 함수
  a = n
  while (n!=0):
    a+=n%10
    n=n//10
  return a

num_list = []
for i in range(1,10000):  # num_list에 생성자의 리스트를 담음
  num_list.append(num(i))

for i in range(1,10000):
  if i not in num_list:   # 1부터 10000까지 반복하면서 숫자가 num_list에 없을 경우 출력
    print(i)              # 셀프넘버이기때문에