from flask import Flask, render_template, Response, send_file, request, jsonify
import requests
import cv2
import numpy as np
import serial
import json
import time
import random
from video_module import generate_frames, generate_frames_origin
            
serial_port1 = '/dev/ttyACM0' # 블루투스 통신
baud_rate = 9600
ser1 = serial.Serial(serial_port1, baud_rate)

app = Flask(__name__, static_url_path='/static')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


@app.errorhandler(404)
def not_found(error):
    return "404 Not Found", 404

@app.route('/test')
def test(error):
    return "404 Not Found"

def is_json(json_str):
    try:
        # json.loads({json_str})
        return True
    except:
        return False
    
@app.route('/save_state', methods=['POST'])
def save_cur_state():
    data = request.json
    with open('state.txt', 'wt') as f:
        data = f.write(str(data))
    return 'Data saved successfully', 200

def generate_inner_json():
    while True:
        with open('inner.txt', 'rt') as f:
            data = f.readline()
        
        if is_json(data):
            yield f'data: {data}\n\n'
        else:
            yield f"data: {json.dumps({'temp': 25.0, 'humidity': 57.0, 'cdc': 419, 'water': 5, 'co2': 825, 'time': '23-09-20 16:51:56'})}\n\n"
        
        time.sleep(1)  # 1초마다 새로운 데이터 생성

def generate_inner_predict_json():
    while True:
        with open('inner_predict.txt', 'rt') as f:
            data = f.readline()
        
        if is_json(data):
            yield f'data: {data}\n\n'
        else:
            yield f"data: {json.dumps({'temp': 25.0, 'humidity': 57.0, 'cdc': 419, 'water': 5, 'co2': 825, 'time': '23-09-20 16:51:56'})}\n\n"
        
        time.sleep(1)  # 1초마다 새로운 데이터 생성

def generate_outter_json():
    while True:
        with open('outter.txt', 'rt') as f:
            data = f.readline()
        
        if is_json(data):
            yield f'data: {data}\n\n'
        else:
            yield f"data: {json.dumps({'temp': 26.72, 'humidity': 56, 'windspeed': 3.84, 'winddeg': '서', 'descript': '가벼운 비'})}\n\n"
        
        time.sleep(1)  # 1초마다 새로운 데이터 생성

def generate_random_data():
    while True:
        # 여기에서 실제 데이터 생성 로직을 구현합니다.
        # 이 예시에서는 무작위로 온도와 습도를 생성합니다.
        temp = round(random.uniform(20, 30), 2)  # 20에서 30 사이의 무작위 온도
        humidity = round(random.uniform(40, 60), 2)  # 40에서 60 사이의 무작위 습도

        data = {
            "temp": temp,
            "humidity": humidity
        }

        yield f"data: {json.dumps(data)}\n\n"
        time.sleep(1)  # 1초마다 새로운 데이터 생성

@app.route('/json_inner')
def json_response1():
    return Response(generate_inner_json(), content_type='text/event-stream')

@app.route('/json_inner_predict')
def json_response2():
    return Response(generate_inner_predict_json(), content_type='text/event-stream')

@app.route('/json_outter')
def json_response3():
    return Response(generate_outter_json(), content_type='text/event-stream')
    # return Response(generate_random_data(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/fanoff")
def fanoff():
    try:
        ser1.write("\n".encode())
        ser1.write("C_F-0\n".encode())  # FAN OFF
        # ser1.write("C_F-0".encode())  # FAN OFF
        # ser1.write("\n".encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    finally:
        return ''
        pass
        # ser1.close()

@app.route("/fanon")
def fanon():
    try:
        ser1.write("\n".encode())
        ser1.write("C_F-1\n".encode())
        # ser1.write("C_F-1".encode())  # FAN ON
        # ser1.write("\n".encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    finally:
        return ''
        pass
        # ser1.close()

@app.route("/lightoff")
def lightoff():
    try:
        ser1.write("\n".encode()) 
        ser1.write("C_L-0\n".encode())  # LIGHT OFF
        # ser1.write("C_L-0".encode())  # LIGHT OFF
        # ser1.write("\n".encode()) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/light2")
def light2():
    try:
        ser1.write("\n".encode()) 
        ser1.write("C_L-2\n".encode())  # LIGHT OFF
        # ser1.write("C_L-2".encode())  # LIGHT OFF
        # ser1.write("\n".encode()) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/light4")
def light4():
    try:
        ser1.write("\n".encode()) 
        ser1.write("C_L-4".encode())  # LIGHT OFF
        ser1.write("\n".encode()) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/light6")
def light6():
    try:
        ser1.write("\n".encode()) 
        ser1.write("C_L-6".encode())  # LIGHT OFF
        ser1.write("\n".encode()) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/light8")   
def light8():
    try:
        ser1.write("\n".encode()) 
        ser1.write("C_L-8".encode())  # LIGHT OFF
        ser1.write("\n".encode()) 
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/lightfull")
def lightfull():
    try:
        ser1.write("\n".encode())
        ser1.write("C_L-10.2".encode())  # LIGHT full
        ser1.write("\n".encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/servoon")
def servoon():
    try:
        ser1.write("\n".encode())
        ser1.write("C_S-1\n".encode())  # SERVO OFF
        # ser1.write("C_S-0".encode())  # SERVO OFF
        # ser1.write("\n".encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")
    return ''
@app.route("/servooff")
def servooff():
    try:
        ser1.write("\n".encode())
        ser1.write("C_S-0\n".encode())  # SERVO ON
        # ser1.write("C_S-1".encode())  # SERVO ON
        # ser1.write("\n".encode())
    except KeyboardInterrupt:
        print("KeyboardInterrupt: 프로그램이 종료되었습니다.")      
    return ''


@app.route("/")
def start():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(generate_frames_origin(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/yolostream')
def yolostream():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')

@app.route('/page404')
def page404():
    return render_template('page404.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/charts')
def charts():
    with open('state.txt', 'rt') as f:
        data = f.readline().strip()  # 파일에서 데이터를 읽고 공백 제거

    return render_template('charts.html', data=data.lower())
    

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/utilities_animation')
def utilities_animation():
    return render_template('utilities_animation.html')

@app.route('/utilities_border')
def utilities_border():
    return render_template('utilities_border.html')

@app.route('/utilities_color')
def utilities_color():
    return render_template('utilities_color.html')

@app.route('/utilities_other')
def utilities_other():
    return render_template('utilities_other.html')

@app.route('/marketing.mp4')
def serve_video():
    # marketing.mp4 파일을 제공합니다.
    return send_file('static/marketing.mp4', as_attachment=True)