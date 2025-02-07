randomNum = [3,1,4,2,5]

for i in range(len(randomNum))
    print(i)
    if randomNum[i] > randomNum[i+1]:
        temp = randomNum[i]
        randomNum[i] = randomNum[i+1]
        randomNum[i+1] = temp

for i in range(4)


print(randomNum)