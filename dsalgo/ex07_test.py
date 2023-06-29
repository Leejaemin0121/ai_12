def moveQueue():
    global SIZE, queue, front, rear

    for i in range(front+1, SIZE):      # 모든 사람을 한칸씩 앞으로 당긴다.
        queue[i - 1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1
    

def deQueue():
    global SIZE, queue, front, rear
    if (front == rear):
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data


SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", "재남"]
front = -1
rear = 4


if __name__ == "__main__":
    
    while 1:    
        print("대기 줄 상태 : ", queue)
        print(deQueue(), "님이 식당에 들어감")
        moveQueue()
        
        if front == rear:
            print("대기 줄 상태 : ", queue)
            print("식당 영업 종료!")
            break