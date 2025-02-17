# da03_stack(2).py
# 응용예제 01. 헨젤과 그레텔의 집으로 돌아가기

import random

SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1

## 함수 선언
def isStackFull():
    global SIZE, stack, top
    if top == (SIZE -1): 
        return True
    else:
        return False
    
def isStackEmpty(): 
    global SIZE, stack, top
    if top == -1 :
        return True
    else:
        return False
    
def push(data): 
    global SIZE, stack, top
    if isStackFull(): 
        print('Stack is full!')
    else:
        top += 1
        stack[top] = data

def pop(): 
    global SIZE, stack, top
    if isStackEmpty():
        # print('Stack is empty')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek():
    global SIZE, stack, pop
    if isStackEmpty():
        print('Stack is Empty')
        return None
    else:
        return stack[top]


if __name__ == '__main__':
    stoneAry =['빨강', ' 파랑', '초록', '노랑', '보라', '주황']
    random.shuffle(stoneAry)

    print('과자집에 가는 길 : ',end=' ')
    for stone in stoneAry:
        push(stone)
        print(f'{stone} -->', end=' ')
    print('과자집')

    print('우리집에 오는 길 : ', end= ' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(f'{stone} -->', end=' ')
    print('우리집')