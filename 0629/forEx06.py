number = int(input("숫자를 입력하세요: "))
for i in range(1, number+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

    