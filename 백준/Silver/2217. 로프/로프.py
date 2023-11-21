N = int(input())
weight = []
answer=[]

for i in range(N):
    weight.append(int(input()))   # weight 빈 배열에 입력받은 값들을 넣음

weight = sorted(weight)           # sort로 오름차순 정렬함

for j in weight:                  # weight에 있는 값들을 반복해서 돌며
    answer.append(j*N)            # answer 빈 배열에 (weight(요소)*로프의 개수)를 넣음
    N -= 1                        # N을 -1해나가면서 weight 값이 커짐에 따라 적은 개수를 곱함

print(max(answer))                # answer에서 가장 큰 값(max)을 출력