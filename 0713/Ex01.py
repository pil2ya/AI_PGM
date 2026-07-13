print("인공지능프로그래밍 시험")  # 첫 문장으로 시험 이름을 화면에 출력함
print("문제1)")  # 문제 번호를 화면에 출력함

scores = [78, 85, 92, 68, 95, 88, 74]  # 주어진 점수 데이터를 scores 리스트에 저장함

# 1.1 평균 점수 계산 및 출력
average_score = round(sum(scores) / len(scores), 2)  # 합계를 개수로 나눈 뒤 소수점 둘째 자리까지 반올림함
print(f"1.1 결과: 평균 점수 = {average_score}점")  # 계산된 평균 점수를 지정된 포맷으로 출력함

# 1.2 최고점과 최저점 출력
max_score = max(scores)  # max 함수를 사용해 리스트에서 가장 높은 점수를 찾음
min_score = min(scores)  # min 함수를 사용해 리스트에서 가장 낮은 점수를 찾음
print(f"1.2 결과: 최고점 = {max_score}점, 최저점 = {min_score}점")  # 최고점과 최저점을 화면에 출력함

# 1.3 80점 이상 리스트 생성
above_80_scores = [s for s in scores if s >= 80]  # scores 리스트에서 80점 이상인 점수(s)만 뽑아 새 리스트를 만듦
print(f"1.3 결과: 80점 이상 점수 리스트 = {above_80_scores}")  # 생성된 80점 이상 점수 리스트를 출력함

# 1.4 평균 이상인 학생 수 출력
above_avg_count = len([s for s in scores if s >= average_score])  # 평균 이상인 점수들만 모아서 그 개수(len)를 구함
print(f"1.4 결과: 평균 이상인 학생 수 = {above_avg_count}명")  # 계산된 학생 수를 화면에 출력함