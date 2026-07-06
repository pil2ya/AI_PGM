def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b


while True:
    print("\n=== 계산기 ===")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")

    choice = input("메뉴를 선택하세요 (1~5): ")

    if choice == "5":
        print("계산기를 종료합니다.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("올바른 메뉴를 선택하세요.")
        continue

    try:
        num1 = float(input("첫 번째 숫자: "))
        num2 = float(input("두 번째 숫자: "))
    except ValueError:
        print("숫자를 입력하세요.")
        continue

    if choice == "1":
        result = add(num1, num2)
        op = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        op = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        op = "*"
    elif choice == "4":
        result = divide(num1, num2)
        op = "/"

    print(f"\n결과: {num1} {op} {num2} = {result}")