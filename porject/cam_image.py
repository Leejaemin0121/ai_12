import cv2

# 웹캠 초기화
cap = cv2.VideoCapture(1)  # 0은 기본 웹캠을 나타냅니다.

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 웹캠 화면 보이기
    cv2.imshow("Webcam", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(100) == ord('q'):
        break

# 웹캠 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
