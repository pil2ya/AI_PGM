coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money >=300:
        coffee -= 1
        print("커피를 제공합니다.")
        print(f"거스름돈은 {money - 300}원 입니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    else:
        print("금액이 부족합니다. 커피를 제공할 수 없습니다")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
    