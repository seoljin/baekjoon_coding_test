A,B = map(int,input().split())
num_list = []
for i in range(1,B+1):
  for j in range(i): 
    num_list.append(i)
# print(num_list)

answer = 0
for k in range(A,B+1):
    answer += num_list[k-1]

print(answer)