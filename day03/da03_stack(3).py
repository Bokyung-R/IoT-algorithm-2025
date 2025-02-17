# da03_stack(3).py
# 응용예제 2. 파일 내용을 완전히 거꾸로 출력하기

SIZE = 100
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
        # print('Stack is full!')
        return
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
        # print('Stack is Empty')
        return None
    else:
        return stack[top]


if __name__=="__main__":
    f = open('./day03/진달래꽃.txt', mode='r', encoding='utf-8')
    lineAry = f.readlines()

    print('----원본----')
    for line in lineAry:
        push(line)
        print(line, end=' ')
    print()

    print('----거꾸로----')
    while True:
        line = pop()
        if line == None:
            break

        miniStack = [None for _ in range(len(line))]
        miniTop = -1

        for ch in line:
            miniTop += 1
            miniStack[miniTop] = ch

        while True:
            if miniTop == -1 :
                break
            ch = miniStack[miniTop]
            miniTop -= 1
            print(ch,end='')