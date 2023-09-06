from ultralytics import YOLO
import matplotlib.pyplot as plt
from PIL import Image


def visualize_detection_results(image_path, result):
    # 이미지 로드
    orig_img = Image.open(image_path)

    # 탐지된 bounding box 정보 가져오기
    boxes = result.boxes[0].cpu()

    # 원본 이미지 시각화
    plt.imshow(orig_img)

    # bounding box 그리기
    for box in boxes:
        x1, y1, x2, y2 = box
        plt.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], linewidth=2)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # 학습된 모델 파일 경로
    model_path = 'C:/test/train2/weights/best.pt'

    # 이미지 파일 경로
    image_path = 'C:/test/V006_77_1_19_11_03_12_1_2851q_20201120_17.jpeg'

    # YOLO 모델 불러오기
    model = YOLO(model_path)

    # 객체 탐지 수행
    results = model(image_path)

    # 결과 시각화
    visualize_detection_results(image_path, results[0])
