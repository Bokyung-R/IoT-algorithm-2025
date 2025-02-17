# da01_linked_list(1).py
# Code04-09 예제

memory = []
head, curr, prev = None, None, None
dataArray = [['지민','010-1111-1111'], ['정국','010-2222-2222'], ['뷔','010-3333-3333'], ['슈가','010-4444-4444'], ['진','010-5555-5555']]

class Node():
    def __init__(self, data=None):
        self.data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link
    
    def getLink(self):
        return self.__link

def printNodes(start):
    curr = start
    if curr is None:
        return
    print(curr.data, end=' ')
    while curr.getLink() is not None:
        curr = curr.getLink()
        print(curr.data, end=' ')
    print()

def makeSLL(namePhone):
    global memory, head, curr, prev

    node = Node(namePhone)  # 생성자에서 data 직접 설정
    memory.append(node)

    if head is None:  # 첫 번째 노드인 경우
        head = node
        return

    if head.data[0] > namePhone[0]:  # 맨 앞에 삽입하는 경우
        node.setLink(head)
        head = node
        return

    # 중간 또는 마지막에 삽입하는 경우
    curr = head
    while curr.getLink() is not None:
        prev = curr
        curr = curr.getLink()
        if curr.data[0] > namePhone[0]:  # 삽입 위치 발견
            prev.setLink(node)
            node.setLink(curr)
            return
        
    curr.setLink(node)  # 마지막 노드에 삽입

if __name__=='__main__':
    for data in dataArray:
        makeSLL(data)

    printNodes(head)
