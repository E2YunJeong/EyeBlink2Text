import dlib
import cv2

# 랜드마크 인덱스 설정
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
EYES = RIGHT_EYE + LEFT_EYE

predictor_path = "../models/shape_predictor_68_face_landmarks.dat"
video_path = "../data/eyeblink8/1/26122013_223310_cam.avi"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

video = cv2.VideoCapture(video_path)
if not video.isOpened():
    raise Exception("영상 파일을 열 수 없습니다.")

while True:
    ret, frame = video.read()
    if not ret:
        break  # 영상 끝에 도달하면 종료

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    if len(faces) > 0:
        face = faces[0]  # 첫 번째 얼굴만 사용

        # 얼굴 박스 그리기
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

        # 랜드마크 추출
        landmarks = predictor(gray, face)

        # 눈 부위 시각화
        for n in EYES:
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

    # 결과 출력
    cv2.imshow("Face and Eyes Detection", frame)

    # ESC 키 누르면 종료
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
