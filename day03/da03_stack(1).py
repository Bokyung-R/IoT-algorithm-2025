# da03_stack(1).py
# Code06-09 

import webbrowser
import time

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

## 함수 선언
def isStackFull(): # 스택이 꽉 찼는지 확인
    global SIZE, stack, top
    if top == (SIZE -1): # Full / 실무에서 쓰틑 스택은 거의 무제한
        return True
    else:
        return False
    
def isStackEmpty(): # 스택이 비었는지 확인
    global SIZE, stack, top
    if top == -1 : # Empty
        return True
    else:
        return False
    
def push(data): # 스택에 데이터 추가
    global SIZE, stack, top
    if isStackFull(): # isStackFull() == True 와 동일
        print('Stack is full!')
        # return 생략
    else:
        top += 1
        stack[top] = data

def pop(): # 스택에서 데이터 추출
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is empty')
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek(): # 스택의 top위치의 데이터 확인(살짝보기)
    global SIZE, stack, pop
    if isStackEmpty():
        print('Stack is Empty')
        return None
    else:
        return stack[top]


if __name__=='__main__':
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls:
        push(url)
        webbrowser.open('http://'+url)
        print(url, end='-->')
        time.sleep(1)

    print('방문 종료')
    time.sleep(5)

    while True:
        url=pop()
        if url == None:
            break
        webbrowser.open('http://'+ url)
        print(url,end='-->')
        time.sleep(1)
    print('방문종료')