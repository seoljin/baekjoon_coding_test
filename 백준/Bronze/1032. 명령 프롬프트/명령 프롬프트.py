N = int(input())
strings = []

# 문자열을 입력받고 리스트에 넣기
for i in range(N):
    strings.append(input())
answer = list(strings[0])   # list의 0번째 값을 리스트로 answer에 넣기

for i in range(1,N):                # (0은 기준으로 빼놓고) 1부터 N까지 반복
   for j in range(len(answer)):     # strings[0]의 길이만큼 반복
    if answer[j] != strings[i][j]:  # answer 인덱스 j의 값이 strings 인덱스 i 문자열의 j번째 글자와 다르면
        answer[j] = '?'               # 해당 글자를 ?로 바꿈
print(''.join(answer))