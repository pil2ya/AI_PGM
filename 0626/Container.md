# Python Containers

Python의 **Container**는 여러 개의 값을 하나의 변수에 담아 관리할 수 있는 자료형입니다.  
대표적으로 `list`, `tuple`, `dict`, `set`이 있으며, 각 자료형은 저장 방식과 사용 목적이 다릅니다. [web:34][web:37]

---

## 목차

1. Container란?
2. 주요 Container 종류
3. Mutable / Immutable
4. Ordered / Unordered
5. 중복 허용 여부
6. 언제 무엇을 쓸까?
7. 기본 예제
8. Container 비교표
9. 정리

---

## 1. Container란?

Container는 여러 객체를 묶어서 저장하는 자료형입니다.  
Python에서는 데이터를 효율적으로 다루기 위해 다양한 container 타입을 제공합니다. [web:34][web:37]

Container는 크게 다음과 같이 나눌 수 있습니다. [web:37]

- Sequence: `list`, `tuple`, `range`, `str`, `bytes`, `bytearray`, `memoryview`
- Set: `set`, `frozenset`
- Mapping: `dict`

---

## 2. 주요 Container 종류

### 2.1 List

`list`는 순서가 있고 변경 가능한 자료형입니다.  
대괄호 `[]`로 만들며, 중복 값을 허용합니다. [web:35][web:37]

```python
fruits = ["apple", "banana", "cherry"]
```

### 2.2 Tuple

`tuple`은 순서가 있지만 변경할 수 없는 자료형입니다.  
소괄호 `()`를 사용하며, 중복 값을 허용합니다. [web:35][web:37]

```python
point = (10, 20)
```

### 2.3 Dictionary

`dict`는 key와 value를 함께 저장하는 mapping 자료형입니다.  
중괄호 `{}`를 사용하고, key는 중복될 수 없으며 value는 중복될 수 있습니다. [web:34][web:37]

```python
person = {
    "name": "Kim",
    "age": 20
}
```

### 2.4 Set

`set`은 중복을 허용하지 않는 집합 자료형입니다.  
중괄호 `{}`를 사용하지만, 빈 set은 `set()`으로 만들어야 합니다. [web:34][web:37]

```python
nums = {1, 2, 3}
empty_set = set()
```

---

## 3. Mutable / Immutable

Container는 수정 가능 여부에 따라 `mutable`과 `immutable`로 나눌 수 있습니다. [web:34][web:35]

- Mutable: `list`, `dict`, `set`
- Immutable: `tuple`, `frozenset`

```python
a =[3][4][5]
a = 10
print(a)  #[4][5][6]
```

```python
b = (1, 2, 3)
# b = 10  # 에러 발생
```

---

## 4. Ordered / Unordered

일부 container는 순서가 있고, 일부는 순서가 없습니다. [web:34][web:37]

- Ordered: `list`, `tuple`, `dict`
- Unordered: `set`, `frozenset`

`list`와 `tuple`은 인덱스로 접근할 수 있고, `dict`는 key를 통해 접근합니다.  
`set`은 인덱스 접근이 불가능하고, membership 확인에 주로 사용됩니다. [web:35][web:37]

---

## 5. 중복 허용 여부

Container마다 중복 값 허용 방식이 다릅니다. [web:35][web:37]

- `list`: 허용
- `tuple`: 허용
- `dict`: key는 중복 불가, value는 중복 가능
- `set`: 중복 불가

```python
items =[5][3][4]
pairs = {"a": 1, "b": 1}
unique = {1, 2, 3}
```

---

## 6. 언제 무엇을 쓸까?

데이터가 자주 바뀌고 순서가 중요하면 `list`가 적합합니다.  
바뀌면 안 되는 고정 정보는 `tuple`이 좋습니다.  
key로 값을 빠르게 찾고 싶으면 `dict`를 사용하고, 중복 제거와 포함 여부 확인이 중요하면 `set`을 사용합니다. [web:32][web:35]

---

## 7. 기본 예제

### List
```python
nums =[3][4][5]
nums.append(4)
print(nums)  #[7][4][5][3]
```

### Tuple
```python
coords = (3, 5)
print(coords)  # 3
```

### Dictionary
```python
student = {"name": "Lee", "score": 95}
print(student["name"])  # Lee
```

### Set
```python
data = {1, 2, 2, 3}
print(data)  # {1, 2, 3}
```

---

## 8. Container 비교표

| Type | Ordered | Mutable | Duplicate | Access |
|---|---:|---:|---:|---|
| `list` | Yes | Yes | Yes | index |
| `tuple` | Yes | No | Yes | index |
| `dict` | Yes | Yes | key unique | key |
| `set` | No | Yes | No | membership |

---

## 9. 정리

Python container는 여러 데이터를 효율적으로 다루기 위한 핵심 자료형입니다.  
`list`, `tuple`, `dict`, `set`의 특징을 구분해서 사용하면 코드 구조를 더 깔끔하게 만들 수 있습니다. [web:34][web:37]
