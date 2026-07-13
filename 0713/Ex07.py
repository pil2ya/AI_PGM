import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
import numpy as np

print("인공지능프로그래밍 시험")
print("문제7) MNIST 파이프라인 검증\n")

# ----------------------------------------------------
# [7.1 데이터 전처리 부분]
# ----------------------------------------------------
# 1. MNIST 데이터셋 로드
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 0~255 사이의 픽셀 값을 0.0~1.0 사이로 정규화(Normalization)
x_train, x_test = x_train / 255.0, x_test / 255.0


# ----------------------------------------------------
# [7.2 모델 생성 부분]
# ----------------------------------------------------
# 28x28 크기의 이미지를 펴서 128개 뉴런을 거쳐 최종 10개(0~9)로 분류하는 신경망 설계
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])


# ----------------------------------------------------
# [7.3 학습 부분]
# ----------------------------------------------------
# 모델의 평가지표를 설정(Compile)하고, 훈련 데이터로 5회(Epochs=5) 반복 학습 진행
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("--- [7.3 학습 시작] ---")
model.fit(x_train, y_train, epochs=5, verbose=1)
print("-----------------------\n")


# ----------------------------------------------------
# [7.4 평가 부분]
# ----------------------------------------------------
# 한 번도 보지 못한 테스트 데이터를 주어 모델의 최종 정확도 측정
print("--- [7.4 평가 시작] ---")
loss, accuracy = model.evaluate(x_test, y_test, verbose=1)
print(f"테스트 정확도: {accuracy * 100:.2f}%\n")


# ----------------------------------------------------
# [7.5 예측 부분]
# ----------------------------------------------------
# 테스트 데이터 중 첫 번째 이미지(x_test[0])를 주고 무엇인지 맞추라고 지시
print("--- [7.5 예측 시작] ---")
predictions = model.predict(x_test[:1], verbose=0)

# 10개의 성공 확률 중 가장 높은 인덱스(숫자)를 정답으로 추출
predicted_number = np.argmax(predictions[0])
print(f"모델이 예측한 실제 손글씨 숫자 결과: {predicted_number}")
print(f"실제 정답(레이블): {y_test[0]}")