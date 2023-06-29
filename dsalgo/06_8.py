
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


SIZE = int(input("스택 크기를 입력하세요 ==> "))
stack = [None for _ in range(SIZE)]
top = -1

## main ##
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    while (select != "X" and select != "x"):
        if select == "I" or select == "i":
            data = input("입력학 데이터 ==> ")
            push(data)
            print("스택 상태: ", stack)
        elif select == "E" or select == "e":
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태: ", stack)
        elif select == "V" or select == "v":
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태: ", stack)
        else:
            print("입력이 잘못됨")
            
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    print("프로그램 종료!")