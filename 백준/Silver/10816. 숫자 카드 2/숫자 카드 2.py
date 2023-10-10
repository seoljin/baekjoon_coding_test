N = int(input())  # 첫 번째 배열에 들어갈 숫자의 개수를 입력
# arr 배열을 오름차순으로 정렬. 오름차순 정렬은 이진 탐색을 위해 필요
arr = sorted(list(map(int, input().split())))
# 두 번째 배열에 들어갈 숫자의 개수를 입력
M = int(input())
# 두 번째 배열의 요소들을 저장.
arr2 = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

# [left_v, right_v] 범위 내에 있는 원소 개수 출력 함수
def cnt_within_range (arr, left_v, right_v):
    # 맨 좌측 인덱스
    left_idx = bisect_left(arr, left_v)
    # 맨 우측 인덱스
    right_idx = bisect_right(arr, right_v)
    return right_idx - left_idx

# 값이 arr2[a]인 원소 개수 출력
for a in range(M):
  print(cnt_within_range(arr, arr2[a], arr2[a]), end=' ')