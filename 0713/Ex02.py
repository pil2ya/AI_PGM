import numpy as np
import pandas as pd

# Pandas 터미널 출력 시 한글 정렬이 깨지는 현상을 방지하는 설정
pd.set_option('display.unicode.east_asian_width', True)

print("인공지능프로그래밍 시험")
print("문제2)")

data = np.array([
    [85, 90, 88],
    [70, 80, 75],
    [95, 98, 100],
    [60, 72, 68]
])

# 2.1 DataFrame으로 변환하시오.
df_basic = pd.DataFrame(data)
print(f"2.1 결과:\n{df_basic}\n")

# 2.2 열 이름을 국어, 영어, 수학으로 지정하시오.
df = pd.DataFrame(data, columns=["국어", "영어", "수학"])
print(f"2.2 결과:\n{df}\n")

# 2.3 학생별 평균을 새로운 열에 추가하시오.
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1).round(2)
print(f"2.3 결과:\n{df}\n")

# 2.4 평균이 가장 높은 학생을 출력하시오.
best_student = df.loc[df["평균"].idxmax()]
print(f"2.4 결과:\n평균이 가장 높은 학생 정보:\n{best_student}")