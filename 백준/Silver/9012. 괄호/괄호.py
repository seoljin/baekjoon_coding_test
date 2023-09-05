import sys

T = int(input())

for i in range(T):
  VPS = input() #list로 받았다가 (이거와 )를 하나로 볼 수 없다는 걸 알게 됨
  while '()' in VPS:
    # VPS = VPS.remove('()') list로 받았다가 하나로 볼 수 없어 안된다는 걸 알게됨
    # 또 스트링은 remove가 안된다는걸 까먹고 썼다가 오류남
    VPS = VPS.replace('()','')

  if len(VPS) ==0 :
    print('YES')
  else:
    print('NO')