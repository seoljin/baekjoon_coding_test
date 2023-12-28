arr = []
for i in range(1,9):
    arr.append(int(input()))

sorted_arr = sorted(arr,reverse=True)

sum = 0
arr_idx = []
for i in range(5):
    sum += sorted_arr[i]
    arr_idx.append( arr.index(sorted_arr[i]) + 1 )

print(sum)
print(*sorted(arr_idx), end=' ')