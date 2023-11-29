import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print('영상 폭:', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('영상 높이:', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('프레임 속도:', cap.get(cv2.CAP_PROP_FPS))

while cap.isOpened():
    ret, img = cap.read()

    if ret:
        cv2.imshow('비디오 캡처', img)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Esc 키를 누르면 종료됩니다.
            break

cap.release()
cv2.destroyAllWindows()