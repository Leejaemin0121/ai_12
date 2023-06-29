import webbrowser
import time

def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return 1
    else:
        return 0
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == - 1):
        return 1
    else:
        return 0
    
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다")
        return None
    return stack[top]

## 전역 변수 선언
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

## main ##
if __name__ == "__main__":
    urls = ["naver.com", "daum.net", "goolge.com"]
    
    for url in urls:
        push(url)
        webbrowser.open("http://" + url)
        print(url, end= "-->")
        time.sleep(2)
        
    print("방문 종료")
    time.sleep(2)
    
    while 1:
        url = pop()
        if url == None:
            break
        webbrowser.open("http://" + url)
        print(url, end= "-->")
        time.sleep(1)
    print("방문 종료")