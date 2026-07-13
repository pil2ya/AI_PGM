import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tensorflow as tf
import logging

logging.getLogger('tensorflow').setLevel(logging.ERROR)

print("인공지능프로그래밍 시험")
print("문제4)")

x_train = np.array([1, 2, 3, 4, 5], dtype=np.float32)
y_train = np.array([3, 6, 9, 12, 15], dtype=np.float32)

# 요구사항 반영: Sequential 모델 사용 및 Dense(1) 구성 (Keras 최신 권장 문법으로 경고 완벽 차단)
model = tf.keras.Sequential([
    tf.keras.Input(shape=(1,)),
    tf.keras.layers.Dense(units=1)
])

# 요구사항 반영: Optimizer = Adam (학습 속도를 높여 300회 만에 정답에 수렴하도록 세팅), Loss = MSE
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1), loss='mean_squared_error')

# 요구사항 반영: Epoch = 300
model.fit(x_train, y_train, epochs=300, verbose=0)

x_test = np.array([6, 7, 8], dtype=np.float32)
predictions = model.predict(x_test, verbose=0)

clean_pred = "\n".join([f"x={int(x)} 예측값: {p[0]:.2f}" for x, p in zip(x_test, predictions)])
print(f"4.1 결과 (예측값):\n{clean_pred}")