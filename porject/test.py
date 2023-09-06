import cv2

# 이미지 로드
# 이미지 경로 (슬래시 사용)
image_path = "C:/test/V006_77_1_19_11_03_12_1_4521q_20201209_8.jpeg"
image = cv2.imread(image_path)
if image is None:
    print("Image not loaded")
else:
    # 이미지 크기 조정
    target_size = (640, 640)
    resized_image = cv2.resize(image, target_size)

    # 라벨링 데이터 파싱
    label = "19 0.565476 0.506614 0.563492 0.892857"
    class_index, x, y, width, height = map(float, label.split())

    # 이미지 크기 구하기
    image_height, image_width, _ = resized_image.shape

    # 경계 상자 좌표 계산
    x_min = int((x - width / 2) * image_width)
    y_min = int((y - height / 2) * image_height)
    x_max = int((x + width / 2) * image_width)
    y_max = int((y + height / 2) * image_height)

    # 경계 상자 그리기
    color = (255, 0, 0)  # 경계 상자
    thickness = 2
    cv2.rectangle(resized_image, (x_min, y_min),
                  (x_max, y_max), color, thickness)

    # 이미지에 클래스 이름 추가
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_thickness = 1
    class_name = "Class 19"  # 클래스 이름
    cv2.putText(resized_image, class_name, (x_min, y_min - 10),
                font, font_scale, color, font_thickness)

    # 이미지 보여주기
    cv2.imshow("Image with Bounding Box", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
