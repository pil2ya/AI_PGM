def get_rect_area(w, h):
    """Calculate the area of a rectangle."""
    return w * h

def main():
    width = float(input("Enter the width of the rectangle: ")
    height = float(input("Enter the height of the rectangle: ")
                   
    area = get_rect_area(width, height)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()

# 12번라인이 있으면 다른데서 main() 함수를 호출할 때,
# 프로그램이 실행될 때 main() 함수가 자동으로 호출되지 않도록 하는 역할을 합니다.
# 이 조건문은 스크립트가 직접 실행될 때만 main() 함수를 호출하도록 보장합니다.
# 만약 이 스크립트가 다른 모듈에서 import 된다면, main() 함수는 호출되지 않습니다.
