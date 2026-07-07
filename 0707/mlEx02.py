from sklearn.datasets import load_iris
import pandas as pd
from sklearn import svm
import plotly.express as px

iris = load_iris()

# [수정 완료] px.DataFrame이 아니라 pd.DataFrame으로 고치고 열 이름과 품종을 채워 넣었습니다.
df = pd.DataFrame(iris.data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df['species'] = [iris.target_names[t] for t in iris.target]

s = svm.SVC(gamma=0.1, C=10) 
s.fit(iris.data, iris.target)    # 학습

# 101번째와 51번째 샘플을 변형하여 새로운 데이터 생성
new_d = [[6.4, 3.2, 6.0, 2.5], [7.1, 3.1, 4.7, 1.35]] 
res = s.predict(new_d)
print("새로운 2개 샘플의 부류는", res)

# petal_length를 제외하여 3차원 공간 구성
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.show(renderer="browser")