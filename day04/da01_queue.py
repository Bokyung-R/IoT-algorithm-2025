# da01_queue.py
# 큐 자료구조 구현

# 초기화
SIZE = int(input('큐 크기를 입력하세요 ==> '))
queue = [None for _ in range(SIZE)]
front = rear = 0

# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear
    # 1. 가장 일반적 로직
    # if rear == SIZE - 1 :
    #     return True
    # else:
    #     return False
    # 2. 개선 로직
    # if rear != SIZE - 1:
    #     return False
    # elif rear == SIZE -1 and front == -1:
    #     return True
    # else:
    #     for i in range(front+1, SIZE):
    #         queue[i-1] = queue[i] # 데이터 앞 빈자리에 첫번째 데이터옮김 
    #         queue[i] = None
        
    #     front -= 1
    #     rear -= 1
    #     return False
    # 3. 원형 큐
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
    else:
        rear = (rear+1) % SIZE
        queue[rear] = data    
    
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[(front+1) % SIZE]
    

if __name__=='__main__':
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) --> ').upper()

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 --> {queue}')
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select == 'V':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 {queue}')
        else:
            print('입력 오류')


# 원형 큐의 경우 전체 크기에서 한 칸을 사용하지 못한다는 특징이 있음 
