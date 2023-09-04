def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if i==0:
            answer.append(arr[i])
        else:
            if arr[i-1]==arr[i]:
                pass
            else:
                answer.append(arr[i])
    return answer