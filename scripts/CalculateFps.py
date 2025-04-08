import cv2
import time     # fps 계산 시 사용

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if cap.isOpened() == False:
    print("Camera is not opened")
    exit(1)

prevTime = time.time() # 이전 프레임이 찍힌 시간 저장

while True:
    # ret : 읽기 성공 여부
    # img : 읽어온 영상 프레임
    ret, img = cap.read()

    if ret == False:
        print("Capture failed")
        break

    # 캠 좌우반전 (없어도 되긴 함, 거울처럼 보이게 하여 익숙함을 주기 위해선 필요)
    img = cv2.flip(img, 1)

    # 프레임 수 계산
    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    # 프레임 수 계산을 지속하기 위해 이전 프레임 처리 시각을 현재 프레임 처리 시각으로 변경
    prevTime = curTime
    fps_str = "FPS : %0.1f" %fps

    # 문자열 표시
    cv2.putText(img, fps_str, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
    cv2.imshow('Camera', img)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()