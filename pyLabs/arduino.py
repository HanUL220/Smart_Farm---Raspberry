import mysql.connector
import serial

# 시리얼 포트 설정 (아두이노와 연결된 포트로 변경해야 함)
ser = serial.Serial('/dev/ttyACM0', 9600)  # 포트 이름과 속도를 아두이노에 맞게 설정

db = mysql.connector.connect(
    host="localhost",
    user="lab",
    password="1234",
    database="smartfarm"
)

curs = db.cursor()

while True:
    # 시리얼 포트에서 데이터 읽기
    try:
        data = ser.readline().decode().strip()
        # 데이터를 쉼표로 분할하여 변수에 할당
        h, t, cdsValue, humi = data.split(',')

        # 변수 출력 (센서 데이터 확인)
        print("온도:", t)
        print("습도:", h)
        print("CDS 값:", cdsValue)
        print("토양 습도:", humi)

        curs.execute("INSERT INTO sensor (Temperature, Humidity, CDS_value, Soil_Humidity) VALUES (%s, %s, %s, %s)",
                     (t, h, cdsValue, humi))
        db.commit()
    except ValueError as e:
        print()

db.close()
