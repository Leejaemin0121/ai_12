import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image

# JSON 파일 경로
json_file_path = 'V001_tom1_39_001_a1_00_20210930_14_00134902_49122255.json'

# JSON 파일 불러오기
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# 이미지 경로
image_path = data["imagePath"]

# 이미지 불러오기
image = Image.open(image_path)

# 라벨링 정보 추출
shapes = data["shapes"]

# 라벨마다 색상 지정
label_colors = {}
unique_labels = set(shape["label"] for shape in shapes)
colors = plt.cm.get_cmap("tab20", len(unique_labels))
for i, label in enumerate(unique_labels):
    label_colors[label] = colors(i)

# 이미지에 박스 그리기
fig, ax = plt.subplots(1, figsize=(10, 10))
ax.imshow(image)

for shape in shapes:
    label = shape["label"]
    points = shape["points"]
    x, y = zip(*points)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    color = label_colors[label]
    rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                             linewidth=2, edgecolor=color, facecolor='none', label=label)
    ax.add_patch(rect)

# 이미지에 라벨 표시
ax.legend()
plt.show()
