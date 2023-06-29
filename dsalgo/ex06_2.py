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
    lyrics = '''진달래꽃
나 보기가 역겨워
가실 때에는
말없이 고이 보내드리오리다.'''
    
    print("----- 원본 -----")
    for i in lyrics:
        push(i)
        print(i, end= "")
    print()
    
    print("----- 거꾸로 처리된 결과 -----")
    while 1:
        i = pop()
        if i == None:
            break
        print(i, end= "")