# 입력 코드
n = int(input())
num_list = list(map(int, input().split()))

add_list = []
add = 0

# 작은수부터 순서대로 정렬
num_list.sort() 

for i in range(len(num_list)):
  add += num_list[i]    # 누적합 add
  add_list.append(add)  # 누적합을 순서대로 리스트에 추가

print(sum(add_list)) # 누적합 합계