N = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 딕셔너리로 해보려다가 실패 후 리스트로 선언..
# for i in range(len(alpha)):                             # 잘 나오는지 확인
#   print(alpha[i])

for i in alpha:         # alpha 리스트에 있는 값들을 돌려가며 반복
  N = N.replace(i,'1')  # 입력받은 N문자열에서 alpha값들이 있으면 1로 변환

print(len(N))           # 변환된 1의 길이 출력