from itertools import combinations

def solution(nums):
    answer = 0
    s= [sum(i) for i in combinations(nums,3)]
    for k in s:
        for j in range(2,k):
            if k%j==0:
                break
        else:
            answer+=1

    return answer