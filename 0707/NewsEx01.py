from datetime import datetime

# 경기 결과 입력 받는 곳
place = input("경기가 열린 곳은? ")
time = input("경기가 열린 시간은? ")
opponent = input("상대 팀은? ")
goals = input("손흥민은 몇 골을 넣었나요? ")
aids = input("도움은 몇 개인가요? ")

# score_me와 score_you는 숫자로 비교해야 하므로 int()로 감싸서 숫자로 바꿉니다.
score_me = int(input("손흥민 팀이 넣은 골 수는? "))
score_you = int(input("상대 팀이 넣은 골 수는? "))

# 기사 작성하는 곳 (날짜 가독성을 높였습니다)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
news = f"[프리미어 리그 속보({current_time})]\n"
news = news + f"손흥민 선수는 {place}에서 {time}에 열린 경기에 출전하였습니다. "
news = news + f"상대 팀은 {opponent}입니다. "

# 숫자 비교로 정상 작동합니다.
if score_me > score_you:
    news = news + f"손흥민 선수의 팀이 {score_me}골을 넣어 {score_you}골을 넣은 상대 팀을 이겼습니다. "
elif score_me < score_you:
    news = news + f"손흥민 선수의 팀이 {score_me}골을 넣어 {score_you}골을 넣은 상대 팀에게 졌습니다. "
else:
    news = news + f"두 팀은 {score_me}대{score_you}로 비겼습니다. "

# 골과 도움 수 비교 (이미 위에서 int로 바꿀 수도 있지만, 기존 구조를 유지했습니다)
if int(goals) > 0 and int(aids) > 0:
    news = news + f"손흥민 선수는 {goals}골에 도움 {aids}개로 승리를 크게 이끌었습니다. "
elif int(goals) > 0 and int(aids) == 0:
    news = news + f"손흥민 선수는 {goals}골로 승리를 이끌었습니다. "
elif int(goals) == 0 and int(aids) > 0:
    news = news + f"손흥민 선수는 골은 없지만 도움 {aids}개로 승리하는 데 공헌하였습니다. "
else:
    news = news + f"아쉽게도 이번 경기에서 손흥민의 발끝은 침묵을 지켰습니다. "

# (앞부분 입력 및 기사 작성 코드는 그대로 유지)

print("\n--- 생성된 기사 ---")
print(news)
print("-------------------\n")

import os
import time
import subprocess
import asyncio
import edge_tts

# edge-tts는 비동기(async) 방식으로 작동해서 실행용 함수를 하나 만듭니다.
async def generate_tts():
    print("마이크로소프트 AI를 이용해 고품질 무료 음성 생성 중...")
    
    # 한국어 여성 아나운서 목소리 (SunHi). 
    # 남성 목소리를 원하시면 'ko-KR-InJoonNeural'로 바꾸면 됩니다!
    VOICE = "ko-KR-SunHiNeural" 
    
    communicate = edge_tts.Communicate(news, VOICE)
    await communicate.save("news_Son.mp3")

# 음성 파일 생성 실행
asyncio.run(generate_tts())

mp3_path = os.path.abspath("news_Son.mp3")


# --- 백그라운드 안전 재생 시스템 (창 안 뜸, 인터넷 안 꺼짐) ---
ps_script = (
    f'$player = New-Object System.Windows.Media.MediaPlayer; '
    f'$player.Open([Uri]"{mp3_path}"); '
    f'$player.Play(); '
    f'Start-Sleep -s 100'
)
cmd = ["powershell", "-WindowStyle", "Hidden", "-Command", ps_script]
player_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 글자 수 기반 정확한 재생 시간 계산
pure_text_len = len([c for c in news if c.isalnum()])
estimated_time = int(pure_text_len * 0.28) + 1 

print(f" 🔊 무료 고품질 AI 음성 재생 시작 (예상 재생 시간: {estimated_time}초)")
print(" [진행 상황] ", end="", flush=True)

for _ in range(estimated_time):
    print(".", end="", flush=True)
    time.sleep(1)

# 재생이 끝나면 소리 내던 파워쉘만 깔끔하게 종료
player_process.terminate()

print("\n\n🎉 돈 한 푼 안 들고 인터넷 창도 안전한 스텔스 뉴스가 완료되었습니다! 😎")