import dlib
import cv2
import numpy as np

# 랜드마크 인덱스 설정
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
EYES = RIGHT_EYE + LEFT_EYE

predictor_path = "../models/shape_predictor_68_face_landmarks.dat"
image_path = "../data/images/happy-1836445_1280.jpg"

image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 오류")


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detector는 리스트 반환
# [(left, top), (right, bottom)] 이게 한 쌍으로, 사진에서 검출한 얼굴 수만큼 나옴
faces = detector(gray, 1)
if len(faces) == 0:
    raise Exception("얼굴을 찾을 수 없습니다.")

for (i, face) in enumerate(faces):
    # 얼굴 영역 사각형으로 표시
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

    # 랜드마크 추출
    landmarks = predictor(gray, face)

    # 눈 부위 시각화
    for n in EYES:
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

cv2.imshow("Face and Eyes Detection", image)
cv2.waitKey(0)