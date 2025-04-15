<h2>1. python 버전 지정</h2>

- python 3.9.13 버전으로 설치
- tensorflow 2.15.0 버전은 python 3.9 버전 이상에서 사용할 수 없음

<h2>2. 라이브러리 설치</h2>

- tensorflow 2.15.0 버전으로 설치
- 2.15.0 이상 버전 설치 시 keras와 버전 충돌 발생
- tensorflow와 keras의 버전은 동일해야 함
- 필수 설치 라이브러리는 다음과 같음

  - opencv-python
  - numpy
  - tensorflow 2.15.0 v
  - scikit-learn
  - dlib
- 특정 버전 라이브러리 설치 방법은 다음과 같음

  - pycharm에서 프로젝트 오픈 후 터미널창에서 다음 명령어 입력
  - pip install tensorflow==2.15.0

- dlib 설치 전 해야할 일

  1. C++ compiler 설치 (visual studio 다운로드 → c++를 사용한 데스크톱 개발 선택)
  2. CMake 설치
  3. dlib 다운로드 (pip install dlib)

     - pip으로 설치가 안 된다면
     - http://dlib.net/
     - 위의 사이트에서 dlib 다운로드 후 압축 해제
     - 아래의 명령어 순차적으로 입력
     - python setup.py build
     - python setup.py install
