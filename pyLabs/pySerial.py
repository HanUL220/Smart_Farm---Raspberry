import serial

ser = serial.Serial('/dev/ttyACM0', 9600)  # 아두이노와 연결된 포트 및 속도 설정

while True:
    data = ser.readline().decode().strip()  # 시리얼 데이터 읽기
    print(data)  # 데이터 확인 (출력은 나중에 데이터베이스에 보내기 위한 단계)

    # 여기에서 MySQL에 데이터를 저장하는 코드를 추가합니다.
