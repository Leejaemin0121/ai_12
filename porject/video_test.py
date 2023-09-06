import cv2
from ultralytics import YOLO

# 학습된 모델 파일 경로
model_path = 'C:/test/train01/weights/best.pt'

# Load the YOLOv8 model
model = YOLO(model_path)

# Open the video file
video_path = 1
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    # 좌우 반전
    flipped_frame = cv2.flip(frame, 1)

    if success:
        # Run Tomato on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Tomato", annotated_frame)

        # Set the window property to be always on top
        cv2.setWindowProperty("Tomato", cv2.WND_PROP_TOPMOST, 1)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
