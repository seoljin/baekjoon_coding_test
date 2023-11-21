N = int(input())
#bong = []
#for i in range(N):
#    bong.append(int(input()))    # 런타임에러(value)
bong = list(map(int, input().split()))
max_bong = 0
kill = 0

# bong

answer = 0

for i in bong:        # 봉우리를 돌아가며
    if i > max_bong:  # 가장 높은 봉우리가 현재의 봉우리보다 작으면
        max_bong = i  # 현재의 봉우리를 높은 봉우리에 넣어줌
        kill = 0      # kill은 초기화
    else:
        kill += 1     # 높은 봉우리가 계속 높은 상태면 kill 수 증가

    # 마지막에 계속 0으로 출력하는 실수를 하다가 고침
    # answer과 kill 중 더 높은 값이 answer이 되는 것으로 바꿔야
    # 마지막에 0이 아닌 정답이 출력됨
    answer = max(answer, kill)

print(answer)