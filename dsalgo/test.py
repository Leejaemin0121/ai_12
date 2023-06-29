with open('lyly.txt', 'r', encoding="UTF-8") as f:  # 'r'은 read의 약자

# 만약 디렉토리 안에 파일을 만들고 싶다면 
# with open('디렉토리 파일명/practice.txt', 'r') as f:


    print(type(f))
    for line in f:

       print(line.strip())