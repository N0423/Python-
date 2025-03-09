
numbers = [4, 2, 1, 5, 3]  # 並び替えたい数
n = len(numbers)

for i in range(n):
    swapped = False
    # 未ソート部分のみを処理
    for j in range(n - i - 1):
        # 大きい順にするため、不等号を変更
        if numbers[j] < numbers[j + 1]:
            # Pythonではこのように値の交換が可能です
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    
    # 交換が発生しなければソート完了
    if not swapped:
        break

print(numbers)  # [5, 4, 3, 2, 1]