N = int(input())  # 첫 번째 배열에 들어갈 숫자의 개수를 입력

# arr 배열을 오름차순으로 정렬. 오름차순 정렬은 이진 탐색을 위해 필요
arr = sorted(list(map(int, input().split())))
# 두 번째 배열에 들어갈 숫자의 개수를 입력
M = int(input())
# 두 번째 배열의 요소들을 저장.
arr2 = list(map(int, input().split()))

# 이진 탐색 함수를 정의.
def binary_search(a):
    start = 0  # 탐색할 범위의 시작 인덱스
    end = len(arr) - 1  # 탐색할 범위의 끝 인덱스
    while start <= end:  # 시작 인덱스가 끝 인덱스보다 작거나 같을 때까지 반복
        mid = (start + end) // 2  # 중앙값의 인덱스를 구함.
        if arr[mid] == a:  # 중앙값이 찾고자 하는 값과 같다면
            return 1  # 1을 반환합니다.
        if arr[mid] > a:  # 중앙값이 찾고자 하는 값보다 크다면
            end = mid - 1  # 끝 인덱스를 중앙값보다 하나 앞으로 옮김.
        else:  # 중앙값이 찾고자 하는 값보다 작다면
            start = mid + 1  # 시작 인덱스를 중앙값보다 하나 뒤로 옮김.
    return 0  # 찾고자 하는 값이 없다면 0을 반환.

# 두 번째 배열의 각 요소에 대해서 이진 탐색을 수행하고 결과를 출력.
for a in arr2:
    print(binary_search(a))