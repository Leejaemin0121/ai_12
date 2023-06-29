def pop():
    global SIZE, stack, top
    if top == None :
        print("stack is full")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3