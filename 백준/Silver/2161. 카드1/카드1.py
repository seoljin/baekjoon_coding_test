from collections import deque     #popleft 및 que를 쓰기위해서는 deque를 import 해야함

N = int(input())
arr = [i for i in range(1,N+1)]   # 먼저 입력숫자만큼 배열을 받아야함
que_ = deque(arr)                 # deque 형태로 만들었다
pop_num = []

while len(que_)>1:                # que_의 개수가 하나가 되기전까지 반복
  pop_num.append(que_.popleft())  # 첫번째로 뺀거를 pop_num에 넣기
  que_.append(que_.popleft())     # 첫번째 뺀 후 다음거를 맨뒤로 보내기

for i in range(len(pop_num)):     # 출력문 => 다른 방법은 없을까?
  print(pop_num[i], end=' ')      # 한줄로 띄어서 쓰려면 end = ' ' 필요

print(que_[0])                    # que_를 출력하면 deque([6]) => 이런식으로 나옴 따라서 index붙여서 출력