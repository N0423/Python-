randomNum = [4,2,1,5,3,3,0,8,94,5,633,8643,4,853,8633,9641,863,644,1245,8643,743,865,93,73] #並び替えたい数

roop = True #trueの間は並び替えを続ける

while(roop):
    #randomの左の数＞右の数ならば右の数と左の数を入れ替える
    for i in range(int(len(randomNum))-1):
        print(i)
        if randomNum[i] > randomNum[i+1]:
            temp = randomNum[i]
            randomNum[i] = randomNum[i+1]
            randomNum[i+1] = temp

    #一つでも左の数＞右の数があったらkenchiをtrueにしてループさせる
    kenchi = False
    for i in range(int(len(randomNum))-1):
        if(randomNum [i]> randomNum[i+1]):
            kenchi = True
            break

    roop = kenchi


print(randomNum)