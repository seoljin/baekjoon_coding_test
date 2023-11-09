num = input().split()
#print(num)

a = sorted(num)
b = sorted(num, reverse=True)

# print(a)
# print(b)

if num == a:
  print('ascending')
elif num == b:
  print('descending')
else:
  print('mixed')
