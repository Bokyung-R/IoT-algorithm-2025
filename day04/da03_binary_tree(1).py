# da03_binary_tree(1).py
# 응용 예제 2. 폴더 및 하위 폴더에 중복된 파일 이름 찾기

import os

memory =[]
root = None
fnameAry = []

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

if __name__ =='__main__':
    fName = 'C:\Program Files\Common Files'
    for dirName, subDirList, fnames in os.walk(fName):
        for fname in fnames:
            fnameAry.append(fname)

    node = TreeNode()
    node.data = fnameAry[0]
    root = node
    memory.append(node)

    dupNameAry = [] # 중복된 파일명이 입력될 list

    for name in fnameAry[1:]:
        node = TreeNode()
        node.data = name
        
        current = root
        while True:
            if name == current.data :
                dupNameAry.append(name)
                break
            if name < current.data :
                if current.left == None:
                    current.left = node
                    memory.append(node)
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    memory.append(node)
                    break
                current = current.right
    
    dupNameAry = list(set(dupNameAry))

    print(f'{fName} 및 그 하위 디렉터리의 중복된 파일 목록 --> ')
    print(dupNameAry)