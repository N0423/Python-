def calculator():
    print("シンプル計算機へようこそ!")
    print("終了するには 'q' を入力してください")
    
    while True:
        print("\n使用可能な演算:")
        print("1: 足し算 (+)")
        print("2: 引き算 (-)")
        print("3: 掛け算 (*)")
        print("4: 割り算 (/)")
        
        choice = input("\n演算を選んでください (1-4): ")
        
        if choice.lower() == 'q':
            print("計算機を終了します。")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("無効な選択です。1から4の数字を入力してください。")
            continue
            
        try:
            num1 = float(input("1つ目の数字を入力: "))
            num2 = float(input("2つ目の数字を入力: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("\nエラー: 0での除算はできません")
                    continue
                result = num1 / num2
                print(f"\n{num1} / {num2} = {result}")
                
        except ValueError:
            print("\nエラー: 有効な数字を入力してください")

if __name__ == "__main__":
    calculator()