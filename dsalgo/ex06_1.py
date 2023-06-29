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
        # print("스택이 비었습니다")
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
    road = ["주황", "초록", "파랑", "보라", "빨강", "노랑"]
    
    print("과자집에 가는길", end= " : ")
    for i in road:
        push(i)
        print(i, end= "-->")
    print("과자집")
    
    print("우리집에 오는길", end= " : ")
    while 1:
        i = pop()
        if i == None:
            break
        print(i, end= "-->")
    print("우리집")