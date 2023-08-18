money = int(input())
change = ['500', '100', '50', '10', '5', '1']
need = 1000-money
answer = 0

for i in range(len(change)):
  if need//int(change[i]) != 0:
    answer += need//int(change[i])
    need = need%int(change[i])
  else:
    continue
    
print(answer)