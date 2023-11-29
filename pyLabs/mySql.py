import serial
import mysql.connector

# MySQL 연결 설정
db = mysql.connector.connect(
    host=192.168.0.42,
    user="your_username",
    password=0000,
    database="your_database"
)

cursor = db.cursor()

ser = serial.Serial('/dev/ttyACM0', 9600)  # 아두이노와 연결된 포트 및 속도 설정

while True:
    data = ser.readline().decode().strip()  # 시리얼 데이터 읽기
    print(data)  # 데이터 확인

    # 시리얼 데이터를 쉼표로 분할하여 여러 값을 얻음
    values = data.split(',')

    # 적절한 데이터 개수 확인 (humidity, temperature, cds_value, soil_humidity)
    if len(values) == 4:
        humidity, temperature, cds_value, soil_humidity = values

        # 센서 데이터를 데이터베이스에 저장
        query = "INSERT INTO sensor_data (humidity, temperature, cds_value, soil_humidity) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (humidity, temperature, cds_value, soil_humidity))
        db.commit()  # 변경 사항을 저장

    # 필요한 경우 추가 데이터 처리 및 대시보드 업데이트를 수행합니다.

# 연결 종료 (무한 루프에서 나오는 경우 실행되지 않음)
db.close()
