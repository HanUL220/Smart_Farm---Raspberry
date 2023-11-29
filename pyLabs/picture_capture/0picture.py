import time
import picamera

def take_photo(file_path):
    with picamera.PiCamera() as camera:
        # 적절한 카메라 설정을 추가할 수 있습니다 (옵션).
        # 예: 카메라 해상도 설정
        camera.resolution = (400, 400)

        camera.start_preview()
        time.sleep(2)  # 카메라 미리보기를 위한 대기 시간
        camera.capture(file_path)
        camera.stop_preview()

if __name__ == "__main__":
    try:
        while True:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            file_name = f"photo_{timestamp}.jpg"
            take_photo(file_name)
            print(f"사진이 {file_name}에 저장되었습니다.")
            time.sleep(5)  # 5초 대기
    except KeyboardInterrupt:
        print("사진 찍기를 종료합니다.")
