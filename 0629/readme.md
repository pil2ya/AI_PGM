# 🐍 Python 기초 학습 정리

Python 기초 문법부터 파일 입출력, 함수, 제어문, 디버깅까지 학습한 내용을 정리한 문서입니다.

---

## 📌 목차
- 제어문
- 반복 제어 (break / continue)
- 디버깅
- 함수
- 출력 옵션 (sep)
- 파일 입출력
- 폴더 / 파일 생성
- sys.argv
- 추가 학습 내용

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
````

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

## continue

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# 3. 디버깅 (Debugging)

* F10: 한 줄씩 실행 (Step Over)
* F11: 함수 안으로 들어가기 (Step Into)
* 중단점(breakpoint) 설정해서 흐름 확인 가능

---

# 4. 함수 (def)

## 기본 함수

```python
def hello(name):
    return f"Hello {name}"
```

## *args

```python
def add(*args):
    return sum(args)
```

## **kwargs

```python
def info(**kwargs):
    print(kwargs)
```

## return 특징

```python
def test():
    return 10
    print("실행 안됨")
```

---

# 5. 출력 옵션 (sep)

```python
print("A", "B", "C", sep="-")
```

---

# 6. 파일 입출력 (File I/O)

## 기본 방식

```python
f = open("test.txt", "w", encoding="utf-8")
f.write("hello")
f.close()
```

## with문 (권장)

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

## 모드

* r: 읽기
* w: 쓰기 (덮어쓰기)
* a: 추가
* r+: 읽기 + 쓰기

## readline / readlines

```python
f.readline()
f.readlines()
```

## encoding

```python
open("file.txt", "w", encoding="utf-8")
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

실행:

```bash
python test.py hello 123
```

결과:

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
    print("error")
```

## 리스트 컴프리헨션

```python
nums = [i * 2 for i in range(5)]
```

## lambda

```python
f = lambda x: x + 10
```

## pathlib

```python
from pathlib import Path

p = Path("C:/doit/test.txt")
```

## 클래스

```python
class Person:
    def __init__(self, name):
        self.name = name
```

---

# 📌 정리

* 제어문 → 흐름 제어
* 함수 → 코드 재사용
* 파일 I/O → 데이터 저장
* sys.argv → 실행 인자
* 디버깅 → 코드 분석
* with문 → 안전한 파일 처리
