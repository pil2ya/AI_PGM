year = int(input("연도를 입력하세요 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}년은 윤년(leap year)입니다.")
else:
    print(f"{year}년은 광년(common year)입니다.")