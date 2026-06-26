# 파이썬 리스트

파이썬 **리스트(list)** 는 여러 개의 값을 하나의 변수에 순서대로 저장할 수 있는 자료형입니다. 리스트는 변경 가능하고, 같은 값을 여러 번 넣을 수 있습니다.

## 1. 리스트의 특징

- 순서가 있습니다.
- 변경할 수 있습니다.
- 중복 값을 허용합니다.
- 여러 자료형을 함께 저장할 수 있습니다.

예를 들어 리스트에는 문자열, 숫자, 불리언 값을 함께 넣을 수 있습니다.

```python
mixed = ["apple", 10, True, 3.14]
print(mixed)
```

## 2. 리스트 생성하기

리스트는 대괄호 `[]`를 사용해서 만듭니다. `list()` 생성자를 사용할 수도 있습니다. 

```python
fruits = ["apple", "banana", "cherry"]
numbers =[3][4][5][6][7]
items = list(("pen", "book", "desk"))
```

## 3. 인덱싱

리스트는 순서가 있기 때문에 각 항목에 인덱스가 있습니다. 인덱스는 0부터 시작합니다. 

```python
fruits = ["apple", "banana", "cherry"]

print(fruits)   # apple
print(fruits)   # banana[3]
print(fruits[-1])  # cherry
```

## 4. 슬라이싱

슬라이싱을 사용하면 리스트의 일부 구간을 잘라서 가져올 수 있습니다.

```python
fruits = ["apple", "banana", "cherry", "grape", "melon"]

print(fruits[1:4])   # ['banana', 'cherry', 'grape']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:])    # ['cherry', 'grape', 'melon']
```

## 5. 값 추가하기

리스트에는 `append()`, `insert()`, `extend()` 같은 메서드로 값을 추가할 수 있습니다. `append()`는 끝에 추가하고, `insert()`는 원하는 위치에 넣습니다. 

```python
fruits = ["apple", "banana"]

fruits.append("cherry")
print(fruits)   # ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)   # ['apple', 'orange', 'banana', 'cherry']
```

## 6. 값 수정하기

리스트는 변경 가능하므로 인덱스를 이용해 특정 값을 바꿀 수 있습니다. 

```python
fruits = ["apple", "banana", "cherry"]

fruits = "orange"[3]
print(fruits)   # ['apple', 'orange', 'cherry']
```

## 7. 값 삭제하기

리스트에서 값을 삭제할 때는 `remove()`, `pop()`, `del`을 사용할 수 있습니다. `remove()`는 특정 값을 삭제하고, `pop()`은 인덱스로 삭제할 수 있습니다. 

```python
fruits = ["apple", "banana", "cherry", "grape"]

fruits.remove("banana")
print(fruits)   # ['apple', 'cherry', 'grape']

fruits.pop()
print(fruits)   # ['apple', 'cherry']

del fruits
print(fruits)   # ['cherry']
```

## 8. 자주 쓰는 리스트 메서드

리스트를 다룰 때 자주 사용하는 메서드는 다음과 같습니다.

- `append(x)`: 끝에 추가합니다.
- `insert(i, x)`: 원하는 위치에 추가합니다.
- `remove(x)`: 특정 값을 삭제합니다.
- `pop([i])`: 값을 꺼내며 삭제합니다.
- `sort()`: 정렬합니다.
- `reverse()`: 순서를 뒤집습니다.
- `count(x)`: 값의 개수를 셉니다.
- `index(x)`: 값의 위치를 찾습니다.

```python
nums =[5][6][7][3]

print(nums.count(1))  # 2
print(nums.index(4))  # 2

nums.sort()
print(nums)           #[6][7][5][3]

nums.reverse()
print(nums)           #[7][5][6][3]
```

## 9. 반복문과 함께 사용하기

리스트는 `for`문과 함께 사용하면 매우 편리합니다. 각 항목을 하나씩 꺼내 처리할 수 있습니다. 

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## 10. 실생활 예시

리스트는 여러 데이터를 모아서 다뤄야 할 때 유용합니다. 예를 들면 다음과 같습니다.

- 학생 이름 목록
- 장바구니 상품 목록
- 오늘 할 일 목록
- 게임 점수 목록

```python
todo = ["공부하기", "운동하기", "독서하기"]
print(todo)
```

## 11. 리스트와 튜플의 차이

리스트는 수정할 수 있지만, 튜플은 수정할 수 없습니다. 그래서 데이터를 바꿔야 할 때는 리스트를, 바꾸지 않을 때는 튜플을 사용하는 경우가 많습니다.

## 12. 정리

파이썬 리스트는 여러 값을 순서대로 저장하고 자유롭게 수정할 수 있는 자료형입니다. 인덱싱, 슬라이싱, 추가, 삭제, 정렬 기능을 잘 익혀두면 다양한 프로그램을 만들 수 있습니다. 
