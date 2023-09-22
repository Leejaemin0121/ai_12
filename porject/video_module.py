import cv2
from ultralytics import YOLO

# 학습된 모델 파일 경로
model_path = '/home/test4/farm/model/train01/weights/best.pt'     # 학습된 모델 경로

# Load the YOLOv8 model
model = YOLO(model_path)
cap = cv2.VideoCapture(0)
# Function to capture video frames


def generate_frames():
    global cap
    # Open the video file
    video_path = 'http://192.168.0.15/mjpeg/1'  # 입력 받을 비디오 경로
    

    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    while cap.isOpened():
        # Read a frame from the video
        try:
            success, frame = cap.read()

        # 좌우 반전
        # flipped_frame = cv2.flip(frame, 1)

            if success:
                # Run Tomato on the frame
                results = model(frame, verbose=False)

                # Visualize the results on the frame
                annotated_frame = results[0].plot()
                # Encode the frame to JPEG format
                ret, buffer = cv2.imencode('.jpg', annotated_frame)
                if not ret:
                    continue
                # Yield the frame in bytes
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
            else:
                pass
        except:
            pass



    # Release the video capture object
    cap.release()
    
def generate_frames_origin():
    global cap
    # Open the video file
    video_path = 'http://192.168.0.15/mjpeg/1'  # 입력 받을 비디오 경로
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)

    while cap.isOpened():
        # Read a frame from the video
        try:
            success, frame = cap.read()

        # 좌우 반전
        # flipped_frame = cv2.flip(frame, 1)

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            # Yield the frame in bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
        except:
            pass

    # Release the video capture object
    cap.release()