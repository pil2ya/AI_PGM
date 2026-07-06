class Television:
    serial_number = 0  #클래스 변수, 모든 객체가 공유하는 변수
    
    def __init__(self, channel, volume, on):    #생성자, 변수 3개
        Television.serial_number += 1  #객체가 생성될 때마다 serial_number 증가
        self.channel = channel
        self.volume = volume
        self.is_on = on
        
    def __str__(self):  #객체 출력
        return f"Television(serial_number={self.serial_number}, channel={self.channel}, volume={self.volume}, is_on={self.is_on})"
    
    def set_channel(self, channel): #채널 설정
        self.channel = channel
    def get_channel(self): #채널 가져오기
        return self.channel
tv1 = Television(11, 10, True)   #객체 생성
tv2 = Television(22, 20, False)  #객체 생성
tv3 = Television(33, 30, True)   #객체 생성

print(tv1)  #tv1 출력
print(tv2)  #tv2 출력
print(tv3)  #tv3 출력
