# 🐍 Python 기초 학습 정리

Python 기초 문법부터 파일 입출력, 함수, 제어문, 디버깅까지 학습한 내용을 정리한 문서입니다.

---

# 📌 목차

* 제어문
* 반복 제어 (break / continue)
* 디버깅
* 함수
* 출력 옵션 (sep)
* 파일 입출력
* 폴더 / 파일 생성
* sys.argv
* 추가 학습 내용

---

# 1. 제어문 (Control Flow)

## if문

```python
x = 10

if x > 0:
    print("양수")
elif x == 0:
    print("0")
else:
    print("음수")
```

## while문

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

## for문

```python
for i in range(5):
    print(i)
```

## match-case (Python 3.10+)

```python
value = 2

match value:
    case 1:
        print("one")
    case 2:
        print("two")
    case _:
        print("other")
```

---

# 2. 반복 제어 (break / continue)

## break

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

출력

```text
0
1
2
3
4
```

## continue

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

출력

```text
0
1
3
4
```

---

# 3. 디버깅 (Debugging)

* **F10** : 한 줄씩 실행 (Step Over)
* **F11** : 함수 안으로 들어가기 (Step Into)
* **Shift + F11** : 함수 밖으로 나오기 (Step Out)
* **F5** : 디버깅 시작 / 계속 실행
* 중단점(Breakpoint)을 설정하여 프로그램의 흐름을 확인할 수 있습니다.

---

# 4. 함수 (Function)

## 기본 함수

```python
def hello(name):
    return f"Hello {name}"

print(hello("Lee"))
```

출력

```text
Hello Lee
```

---

## *args

```python
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))
```

출력

```text
10
```

---

## **kwargs

```python
def info(**kwargs):
    print(kwargs)

info(name="Lee", age=20)
```

출력

```text
{'name': 'Lee', 'age': 20}
```

---

## return 특징

```python
def test():
    return 10
    print("실행 안됨")

print(test())
```

출력

```text
10
```

> `return`을 만나면 함수는 즉시 종료되므로 그 아래 코드는 실행되지 않습니다.

---

# 5. 출력 옵션 (sep)

```python
print("A", "B", "C", sep="-")
```

출력

```text
A-B-C
```

---

# 6. 파일 입출력 (File I/O)

## 기본 방식

```python
f = open("test.txt", "w", encoding="utf-8")
f.write("hello")
f.close()
```

---

## with문 (권장)

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

> `with`문을 사용하면 파일을 자동으로 닫아주므로 가장 많이 사용하는 방법입니다.

---

## 파일 열기 모드

| 모드   | 설명                      |
| ---- | ----------------------- |
| `r`  | 읽기                      |
| `w`  | 쓰기 (기존 내용 덮어쓰기)         |
| `a`  | 파일 끝에 내용 추가             |
| `x`  | 새 파일 생성 (이미 존재하면 오류)    |
| `r+` | 읽기 + 쓰기                 |
| `w+` | 읽기 + 쓰기 (기존 내용 삭제 후 시작) |
| `a+` | 읽기 + 추가                 |

---

## readline() / readlines()

```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.readline())    # 첫 번째 줄
    print(f.readlines())   # 나머지 줄을 리스트로 반환
```

---

## encoding

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요")
```

---

# 7. 폴더 / 파일 생성

```python
import os

os.makedirs("C:/doit", exist_ok=True)

with open("C:/doit/test.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

---

# 8. sys.argv

```python
import sys

print(sys.argv)
```

실행

```bash
python test.py hello 123
```

출력

```python
['test.py', 'hello', '123']
```

---

# 9. 추가 학습 내용

## try-except

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
```

---

## 리스트 컴프리헨션 (List Comprehension)

```python
nums = [i * 2 for i in range(5)]

print(nums)
```

출력

```text
[0, 2, 4, 6, 8]
```

---

## lambda

```python
f = lambda x: x + 10

print(f(5))
```

출력

```text
15
```

---

## pathlib

```python
from pathlib import Path

p = Path("C:/doit/test.txt")

print(p.name)
print(p.suffix)
```

출력

```text
test.txt
.txt
```

---

## 클래스 (Class)

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Lee")

print(person.name)
```

출력

```text
Lee
```

---

# 📌 정리

* **제어문** → 프로그램의 실행 흐름을 제어
* **함수** → 코드 재사용
* **파일 입출력(File I/O)** → 데이터 저장 및 읽기
* **sys.argv** → 명령행 인자 전달
* **디버깅** → 코드 실행 과정 분석 및 오류 확인
* **with문** → 파일을 안전하게 열고 자동으로 닫음
* **try-except** → 예외 처리
* **리스트 컴프리헨션** → 리스트를 간결하게 생성
* **lambda** → 간단한 익명 함수 작성
* **pathlib** → 파일 및 폴더 경로를 객체 형태로 관리
