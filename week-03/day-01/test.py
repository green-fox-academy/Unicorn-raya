def diff_num4each_position(digits):
    numberIneachPos = []
    for di in digits:
        numberIneachPos.append(di)
    for i in range(len(numberIneachPos)):
        for j in range(i + 1,len(numberIneachPos)):
            if numberIneachPos[i] == numberIneachPos[j]:
                return False
    return True

print(diff_num4each_position("4231"))