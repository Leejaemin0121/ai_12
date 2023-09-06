import json
import cv2

# JSON 파일 경로
json_file_path = "V001_tom1_39_001_a1_00_20210930_14_00134902_49122255.json"

# JSON 파일 읽기
with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

# 이미지 경로 가져오기
image_path = data["imagePath"]

# 이미지 불러오기
image = cv2.imread(image_path)

# 이미지 크기 반으로 축소
resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# 좌표 크기도 반으로 축소된 비율로 조정
resize_ratio = 0.5
resized_points = [[int(x * resize_ratio), int(y * resize_ratio)]
                  for x, y in data["shapes"][0]["points"]]

# 좌표 표시
for x, y in resized_points:
    cv2.circle(resized_image, (x, y), 5, (0, 255, 0), -1)  # 녹색 원으로 표시

# 선 그리기
for i in range(len(resized_points) - 1):
    x1, y1 = resized_points[i]
    x2, y2 = resized_points[i + 1]
    cv2.line(resized_image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 파란색 선으로 표시

# 라벨링 정보를 박스로 표시
label_text = data["shapes"][0]["label"]
label_box_position = (resized_image.shape[1] - 150, 10)
label_box_size = (140, 40)
cv2.rectangle(resized_image, label_box_position,
              (label_box_position[0] + label_box_size[0], label_box_position[1] + label_box_size[1]), (0, 0, 0), -1)

# 폰트 설정 및 라벨링 정보 표시
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(resized_image, label_text,
            (label_box_position[0] + 10, label_box_position[1] + 30), font, 0.9, (255, 255, 255), 1)

# 크기 줄인 이미지 보여주기
cv2.imshow("Image with Points, Lines, and Label", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
