def menu():
    print("1. 섭씨온도 -> 화씨온도")
    print("2. 화씨온도 -> 섭씨온도")
    print("3. 종료")
    selection = input("메뉴를 선택하세요: ")
    return selection

def ctof(c):
    temp = c * 9 / 5 + 32
    return temp

def ftoc(f):
    temp = (f - 32) * 5 / 9
    return temp

def input_f():
    f = float(input("화씨온도를 입력하세요: "))
    return f
    
def input_c():
    c = float(input("섭씨온도를 입력하세요: "))
    return c

def main():
    while True:
        selection = menu()
        if selection == "1":
            c = input_c()
            f = ctof(c)
            print(f"{c}°C는 {f}°F입니다.")
        elif selection == "2":
            f = input_f()
            c = ftoc(f)
            print(f"{f}°F는 {c}°C입니다.")
        elif selection == "3":
            print("프로그램을 종료합니다.")
        else:
            break
main()