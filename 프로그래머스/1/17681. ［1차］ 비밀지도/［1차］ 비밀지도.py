def solution(n, arr1, arr2):
    answer = []
    arr3 = []
    arr4 = []
    num1 = 0
    num2 = 0

    for i in range(n):
        arr3.append([])
        num1 = int(arr1[i])
        arr3[i].append(bin(num1)[2:].rjust(n, "0"))

    for j in range(n):
        arr4.append([])
        num2 = int(arr2[j])
        arr4[j].append(bin(num2)[2:].rjust(n, "0"))

    for k in range(n):
        temp = ''
        for l in range(n):
            if arr3[k][0][l] == '1' or arr4[k][0][l] == '1':
                temp += '#'
            else:
                temp += ' '
            # elif arr3[k][l] == 0 and arr4[k][l] == 0:
            #     temp += ' '
        answer.append(temp)
        
    return answer