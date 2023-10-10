N,M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees) # 시작과 끝 값 설정 → end가 결과값이 된다

while start <= end:
  height = 0
  mid = (start+end)//2 # 중간값

  for tree in trees:
    if tree>mid:
      height += tree - mid # 자른 후 가져갈 수 있는 길이 합

  if height < M: # 가져갈 수 있는 나무 길이 합이 M보다 작은 경우
    end = mid - 1 # 높이 낮추기
  else:
    start = mid + 1 # 높이 높이기

print(end)