# da03_min_cost_spanningtree(1).py
# 응용 예제 1. 허니버터칩이 가장 많이 남은 편의점 찾기

# 전역 변수
G = None
storeAry = [['GS25',30], ['CU',60], ['Seven11', 10], ['MiniStop', 90],['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0,1,2,3,4

# 그래프 클래스
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

                
def printGraph(g):
    global storeAry 
    print('\t',end='')
    for v in range(g.SIZE):
        print(f'{storeAry[v][0]:>9s}', end=' ')
    print()

    for row in range(g.SIZE):
        print(f'{storeAry[row][0]:>9s}',end=' ')
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>8d}', end=' ')
        print()
    print()

## 메인코드 부분
SIZE = 5
G = Graph(SIZE)
G.graph[GS25][CU] = 1;  G.graph[GS25][Seven11] = 1
G.graph[CU][GS25] = 1;  G.graph[CU][Seven11] = 1;   G.graph[CU][MiniStop] = 1
G.graph[Seven11][GS25] = 1; G.graph[Seven11][CU] = 1;   G.graph[Seven11][MiniStop] = 1
G.graph[MiniStop][Seven11] = 1; G.graph[MiniStop][CU] = 1; G.graph[MiniStop][Emart24] = 1
G.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
printGraph(G)

stack = []
visitedAry = []

current = 0
maxStore = current
maxCount = storeAry[current][1] # 편의점에 있는 허니버터 숫자
stack.append(current)
visitedAry.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(SIZE):
        if G.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)

        if storeAry[current][1] > maxCount:
            maxCount = storeAry[current][1]
            maxStore = current
    else:
        current = stack.pop()

print(f'허니버터칩 최대 보유 편의점 (개수) --> {storeAry[maxStore][0]}({storeAry[maxStore][1]})')