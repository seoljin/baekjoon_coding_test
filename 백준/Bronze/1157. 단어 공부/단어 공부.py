words = input().upper() # 대소문자 구별없이 받음

words_set = list(set(words)) # set으로 중복제거
a = []

for word in words_set:
  num = words.count(word) # 한 글자당 갯수를 카운트
  a.append(num)           # 카운트한 숫자를 리스트에 넣음

if a.count(max(a)) >=2:   # 카운트한 숫자 리스트의 가장 큰 값의 개수를 세어
  print('?')              # 2개 이상이면 '?' 출력
else:
  print(words_set[a.index(max(a))]) # 아니면 인덱스 뽑아서 글자 출력