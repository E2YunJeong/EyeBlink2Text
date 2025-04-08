import cv2
import time

video_path = '../data/eyeblink8/1/26122013_223310_cam.avi'  # 영상 파일 경로

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Video file cannot be opened")
    exit(1)

# 원본 영상의 FPS 불러오기
original_fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = int(1000 / original_fps)  # 프레임 간 시간 (ms)

prevTime = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video playback finished or failed")
        break

    # 실제 처리 속도 측정용 FPS
    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    prevTime = curTime
    fps_str = "FPS : %0.1f" % fps

    # 화면에 FPS 표시
    cv2.putText(frame, fps_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Video', frame)

    key = cv2.waitKey(wait_time)

    if key == 27:  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()
