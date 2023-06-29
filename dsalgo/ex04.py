class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end=" ")
    while current.link != None:
        current = current.link
        print(current.data, end=" ")
    print()


def makeSimpleLinkedList(email):
    global memory, head, current, pre
    printNodes(head)
    
    node = Node()
    node.data = email
    memory.append(node)
    if head == None:    #첫 노드일 때
        head = node
        return
    
    if head.data[1] > email[1]:  #첫 노드보다 작을 때
        node.link = head
        head = node
        return
    
    #중간 노드로 삽입하는 경우
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > email[1]:
            pre.link = node
            node.link = current
            return
        
    #삽입하는 노드가 가장 큰 경우
    current.link = node
    
    
memory = []
email = []
head, current, pre = None, None, None
 
if __name__ == "__main__":
    while 1:
        data = input("이름--> ")
        email = input("이메일--> ")
        makeSimpleLinkedList([data, email])
        printNodes(head)
    