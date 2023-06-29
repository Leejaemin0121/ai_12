def isQueueFull():
    global SIZE, queue, front, rear
    # if (rear != SIZE-1):
    #     return False
    if(rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i - 1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
        
        
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data
    

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if (front == rear):
        print("큐가 비었습니다.")
        queue[front] = None
    return queue[front + 1]


SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", "재남"]
front = -1
rear = 4


if __name__ == "__main__":
    
    while 1:
        
        print("대기 줄 상태 : ", queue)
        print(peek(), "님이 식당에 들어감")
        deQueue()
        isQueueFull()
        
        if isQueueEmpty():
            break
    print("대기 줄 상태 : ", queue)
    print("식당 영업 종료!")