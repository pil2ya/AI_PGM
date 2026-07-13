# 🐍 Python 학습 정리

Python 기초 문법부터 머신러닝, 데이터 분석, 입력 처리, 자동화까지 학습한 내용을 정리합니다.

---

# 1. 머신러닝 기초 - 선형 회귀 (Linear Regression)

## 수업 내용 추측

이번 수업에서는 Python을 활용한 머신러닝 기본 흐름을 학습했습니다.

주요 내용:

- Python 외부 라이브러리 사용 방법
- 머신러닝 모델 생성
- 데이터 입력과 결과값 학습
- 학습된 모델을 이용한 예측
- 데이터 시각화

---

# 1-1. 사용 라이브러리

## matplotlib

```python
import matplotlib.pyplot as plt
```

데이터를 그래프로 표현하기 위한 라이브러리입니다.

주요 기능:

- 산점도 그래프 (`scatter`)
- 선 그래프 (`plot`)
- 그래프 출력 (`show`)

---

## scikit-learn

```python
from sklearn import linear_model
```

머신러닝 모델을 제공하는 라이브러리입니다.

이번 코드에서는 선형 회귀 모델을 사용합니다.

---

# 1-2. 선형 회귀 모델 생성

```python
reg = linear_model.LinearRegression()
```

LinearRegression 객체를 생성합니다.

선형 회귀는 데이터의 관계를 찾아서

```
결과 = 입력값의 관계식
```

을 만드는 머신러닝 방법입니다.

예:

```
키 → 몸무게 예측
```

---

# 1-3. 데이터 준비

## 입력 데이터(X)

```python
X = [[174], [152], [138], [128], [186]]
```

머신러닝 모델에 넣어주는 데이터입니다.

이번 예제에서는 사람의 키입니다.

---

## 정답 데이터(y)

```python
y = [71, 55, 46, 38, 88]
```

입력 데이터에 대한 실제 결과값입니다.

예:

```
키 174cm → 몸무게 71kg
```

---

# 1-4. 모델 학습

```python
reg.fit(X, y)
```

fit()은 모델을 학습시키는 함수입니다.

흐름:

```
입력 데이터(X)
+
정답 데이터(y)

↓

패턴 학습

↓

예측 가능한 모델 생성
```

---

# 1-5. 예측

```python
reg.predict([[178]])
```

학습된 모델에게 새로운 데이터를 전달합니다.

예:

```
178cm인 사람의 예상 몸무게
```

---

# 1-6. 데이터 시각화

## 산점도

```python
plt.scatter(X, y, color='blue')
```

실제 데이터를 점으로 표시합니다.

---

## 회귀선 표시

```python
plt.plot(X, reg.predict(X), color='red')
```

학습된 예측 결과를 선으로 표시합니다.

---

# 핵심 개념 정리

- `import` : 외부 라이브러리 사용
- `객체 생성` : 클래스를 이용해 기능 사용
- `fit()` : 머신러닝 학습
- `predict()` : 새로운 데이터 예측
- `list` : 여러 데이터를 저장하는 자료형


---

# 2. 머신러닝 분류 - SVM과 Iris 데이터 분석

## 수업 내용 추측

이번 수업에서는 머신러닝 분류(Classification)와 데이터 시각화를 학습했습니다.

주요 내용:

- sklearn 데이터셋 사용
- pandas 데이터 처리
- SVM 모델 학습
- 새로운 데이터 분류
- 3D 데이터 시각화

---

# 2-1. Iris 데이터셋

```python
from sklearn.datasets import load_iris
```

Iris(붓꽃) 데이터셋을 불러옵니다.

대표적인 머신러닝 학습용 데이터입니다.

데이터:

```
꽃받침 길이
꽃받침 너비
꽃잎 길이
꽃잎 너비

↓

꽃 종류 분류
```

---

# 2-2. pandas DataFrame

```python
import pandas as pd
```

pandas는 데이터를 표 형태로 관리하는 라이브러리입니다.

예:

|sepal_length|species|
|-|-|
|5.1|setosa|

---

# 2-3. DataFrame 생성

```python
df = pd.DataFrame(...)
```

Python 데이터를 표 형태로 변환합니다.

엑셀과 비슷한 형태로 데이터를 관리할 수 있습니다.

---

# 2-4. SVM 모델 생성

```python
from sklearn import svm

s = svm.SVC(gamma=0.1, C=10)
```

SVM(Support Vector Machine)은 데이터를 분류하는 머신러닝 알고리즘입니다.

예:

```
꽃 데이터 입력

↓

Setosa
Versicolor
Virginica

중 하나로 분류
```

---

# 2-5. 모델 학습

```python
s.fit(iris.data, iris.target)
```

입력 데이터와 정답 데이터를 이용해 학습합니다.

---

# 2-6. 예측

```python
res = s.predict(new_d)
```

새로운 데이터를 입력하면 분류 결과를 반환합니다.

---

# 2-7. plotly 시각화

```python
import plotly.express as px
```

인터랙티브 그래프를 만드는 라이브러리입니다.

---

# 핵심 개념 정리

- DataFrame → 데이터를 표 형태로 관리
- 머신러닝 과정

```
데이터 준비
↓
모델 생성
↓
학습(fit)
↓
예측(predict)
```

- 분류(Classification)
  - 데이터를 특정 그룹으로 나누는 방법


---

# 3. Python 입력 처리와 자동 뉴스 생성 프로그램

## 수업 내용 추측

이번 수업에서는 Python 기본 문법과 자동화 프로그램 제작을 학습했습니다.

주요 내용:

- 사용자 입력(input)
- 자료형 변환
- 조건문
- 문자열 조합
- 날짜 처리
- 파일/프로그램 실행
- 비동기 처리
- 음성 생성 자동화

---

# 3-1. 사용자 입력

```python
input()
```

사용자로부터 값을 입력받습니다.

예:

```python
name = input("이름:")
```

입력값은 기본적으로 문자열(str)입니다.

---

# 3-2. 자료형 변환

```python
int(input())
```

문자열을 숫자로 변경합니다.

예:

```python
score = int(input())
```

---

# 3-3. 조건문

```python
if score_me > score_you:
```

조건에 따라 다른 코드를 실행합니다.

구조:

```python
if 조건:
    실행
elif 조건:
    실행
else:
    실행
```

---

# 3-4. f-string

```python
f"손흥민은 {goals}골"
```

문자열 안에 변수를 쉽게 넣는 방법입니다.

기존 방식:

```python
"골 수 : " + str(goals)
```

보다 편리합니다.

---

# 3-5. datetime

```python
from datetime import datetime
```

날짜와 시간을 처리하는 모듈입니다.

```python
datetime.now()
```

현재 시간을 가져옵니다.

---

# 3-6. 함수 생성

```python
async def generate_tts():
```

함수를 정의합니다.

기본 구조:

```python
def 함수이름():
    실행 코드
```

---

# 3-7. 비동기 처리

```python
async
await
```

시간이 오래 걸리는 작업을 처리하기 위한 방식입니다.

예:

- 음성 생성
- 네트워크 작업
- 파일 처리

---

# 3-8. 외부 프로그램 실행

```python
subprocess.Popen()
```

Python에서 다른 프로그램을 실행할 수 있습니다.

예:

```
Python
 ↓
PowerShell 실행
 ↓
음성 파일 재생
```

---

# 3-9. 운영체제 관련 모듈

## os

```python
import os
```

파일 경로, 운영체제 기능 사용

예:

```python
os.path.abspath()
```

절대 경로 확인

---

## time

```python
import time
```

시간 관련 기능

예:

```python
time.sleep(1)
```

1초 대기

---

# 핵심 Python 기본 개념 정리

## 변수

```python
name = "Python"
```

값을 저장하는 공간

---

## 리스트

```python
data = [1,2,3]
```

여러 값을 저장

---

## 조건문

```python
if 조건:
```

상황에 따라 실행 결정

---

## 함수

```python
def function():
```

코드를 재사용하기 위한 구조

---

## 모듈

```python
import 모듈명
```

다른 사람이 만든 기능 사용

---

# 📌 전체 학습 요약

## 머신러닝

```
데이터 준비
↓
모델 생성
↓
fit() 학습
↓
predict() 예측
↓
결과 확인
```

---

## Python 기본 흐름

```
입력(input)
↓
데이터 처리
↓
조건 판단(if)
↓
결과 생성
↓
출력(print)
```

---

## 이번 수업에서 반드시 기억할 Python 개념

- 변수
- 리스트
- 함수
- 객체
- 클래스
- import
- 조건문
- 문자열 처리
- 자료형 변환
- 외부 라이브러리 사용
- 예외 처리
- 비동기 처리
