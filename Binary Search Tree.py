class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

import queue
def levelWiseInput():
    q = queue.Queue()
    print("Enter Data-")
    rootInp = int(input())
    if(rootInp==-1):
        return None
    root = BinaryTreeNode(rootInp)
    q.put(root)
    while(not(q.empty())):
        curr = q.get()
        print("Enter left Node of-",curr.data)
        left = int(input())
        if left!=-1:
            lefty = BinaryTreeNode(left)
            curr.left = lefty
            q.put(lefty)

        print("Enter right node of-",curr.data)
        right = int(input())
        if right!=-1:
            righty = BinaryTreeNode(right)
            curr.right = righty
            q.put(righty)
    return root

def printDetailedTree(root):
    if (root==None):
        return
    print(root.data,end=" ")
    if(root.left!=None):
        print(":- L",root.left.data,end=" ")
    if(root.right!=None):
        print("R",root.right.data,end="")
    print()
    printDetailedTree(root.left)
    printDetailedTree(root.right)

def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif x<root.data:
        search(root.left,x)
    else:
        search(root.right,x)

root = levelWiseInput()
print(printDetailedTree(root))
s = search(root,2)
print(s)