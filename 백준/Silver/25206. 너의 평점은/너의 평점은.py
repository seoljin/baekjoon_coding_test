import sys

# 등급과 학점 선언
grade = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

a = 0
b = 0

for i in range(20): # 20번 반복
  info = list(sys.stdin.readline().split()) # 정보 입력받기
  if info[2] != "P":                        # 정보 split한 것에서 [2]가 P가 아닐 때 반복
    a += score[grade.index(info[2])] * float(info[1]) # 등급에 맞는 점수를 뽑고, 학점과 곱해서 더하기 반복
    b += float(info[1])
    
print(a/b)