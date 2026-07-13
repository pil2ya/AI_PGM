import os

# 1.oneDNN 가속 알림을 원천 차단 (메세지에서 요구한 해결책)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# 2. TensorFlow 내부 C++ 로그 차단
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tensorflow as tf

# 3. 파이썬 내부 tensorflow 로거 경고 등급 설정
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)

print("인공지능프로그래밍 시험")
print("문제3)")

array = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
])

# 3.1 Tensor로 변환 (각 숫자를 2자리 크기로 고정하여 완벽하게 열 정렬)
tensor = tf.convert_to_tensor(array)
clean_tensor_str = "\n".join([
    "[" + " ".join([f"{num:2d}" for num in row]) + "]" 
    for row in tensor.numpy()
])
print(f"3.1 결과:\n{clean_tensor_str}\n")

# 3.2 shape 출력
print(f"3.2 결과: Tensor의 Shape = {tensor.shape}\n")

# 3.3 dtype 출력
print(f"3.3 결과: Tensor의 Dtype = {tensor.dtype}\n")

# 3.4 모든 값에 10을 더한 결과 출력 (3.1과 동일한 정렬 규칙 적용)
tensor_plus_10 = tensor + 10
clean_plus_10_str = "\n".join([
    "[" + " ".join([f"{num:2d}" for num in row]) + "]" 
    for row in tensor_plus_10.numpy()
])
print(f"3.4 결과:\n{clean_plus_10_str}")