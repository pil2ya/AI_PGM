a=(int(input("첫번째 숫자 : ")))
b=(int(input("두번째 숫자 : ")))
print(f" a + b : {a} + {b}")
print(f" a - b : {a} - {b}")
print(f" a * b : {a} * {b}")
print(f" a / b : {a} / {b}")

c=(int(input("첫번째숫자 : " )))
d=(int(input("두번째숫자 : " )))
e=(int(input("세번째숫자 : " )))
f=(int(input("네번째숫자 : " )))
g=(int(input("다섯번째숫자 : " )))
numbers = [c,d,e,f,g]
print(f"정수 5개의 합 : {sum(numbers)}")
print(f"정수 5개의 평균 : {sum(numbers) / len(numbers)}")
print(f"정수 5개의 최소값 : {min(numbers)}")
print(f"정수 5개의 최대값 : {max(numbers)}")

fruits = [apple, banana, orange, grape, melon] = ["사과", "바나나", "오렌지", "포도", "멜론"]
print(f"과일의 첫번째와 마지막 문자열 : {fruits[0]} and {fruits[-1]}")

fruits2=[]
fruit = input("과일을 입력하세요 : ")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")
fruits2.append(fruit)
print(f"입력한 과일 : {fruits2}")

print(fruits2)
print(fruits2[0])
print(fruits2[-1]) 