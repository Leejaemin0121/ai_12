import random
import math


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return

    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], "편의점 거리: ",  math.sqrt(x ** 2 + y ** 2))
    print()


def make_store(store):
    global memory, head, current, pre    
        
    node = Node()                       # 새스토어를 node객체로 생성
    node.data = store
    memory.append(node)
    
    if head == None:                    #만약 head가없다면
        head = node                     #새스토어를 head로 만듬
        node.link = head
        return
    
    # 새스토어 거리 계산
    nodeX, nodeY = node.data[1:]
    node_dist = math.sqrt(nodeX ** 2 + nodeY ** 2)
    # head 거리 계산
    headX, headY = head.data[1:]
    head_dist = math.sqrt(headX ** 2 + headY ** 2)
    
    if head_dist > node_dist:           #만약 head 거리가 새스토어 거리보다 작으면
        node.link = head                
        last = head
        while last.link != head:        #마지막 스토어까지 반복 해줘
            last = last.link
        last.link = node
        head = node
        return
    
    current = head   # 중간에 데이터를 넣을 경우
        
    while current.link != head:
        pre = current
        current = current.link
        
        curX, curY = current.data[1:]
        current_dist = math.sqrt(curX ** 2 + curY ** 2)
        
        if current_dist > node_dist:
            pre.link = node
            node.link = current
            return
        
    current.link = node
    node.link = head
        

## 전역 변수 선언
memory = []
head, current, pre = None, None, None

##메인 코드
if __name__ == "__main__":
    
    storeArray = []
    storeName = "A"
    
    for _ in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        storeArray.append(store)
        storeName = chr(ord(storeName) + 1)
    

    for store in storeArray:  #두 번째 이후 노드
        make_store(store)
        

    printNodes(head)
    