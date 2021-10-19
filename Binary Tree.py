class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def printTree(root):
    if (root==None):
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

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

def treeInput():
    rootTreeInp = int(input())
    if rootTreeInp==-1:
        return None
    root = BinaryTreeNode(rootTreeInp)
    leftInp = treeInput()
    rightInp = treeInput()
    root.left = leftInp
    root.right = rightInp
    return root

def height(root):
    if(root==None):
        return 0
    left = height(root.left)+1
    right = height(root.right)+1
    return max(left,right)

def numNodes(root):
    if root==None:
        return 0
    left = numNodes(root.left)
    right = numNodes(root.right)
    return 1 + left + right

def preOrder(root):
    if(root==None):
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if(root==None):
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def largetData(root):
    if(root==None):
        return -1
    left = largetData(root.left)
    right = largetData(root.right)
    return max(left,right,root.data)

def leafNodes(root):
    if(root==None):
        return 0
    if(root.left==None and root.right==None):
        return 1
    left = leafNodes(root.left)
    right = leafNodes(root.right)
    return left + right

def atKNodes(root,k):
    if root==None:
        return
    if k==0:
        print(root.data)
    atKNodes(root.left,k-1)
    atKNodes(root.right,k-1)

def removeLeaves(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root

def height(root):
    if root==None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def isBalance(root):
    if root==None:
        return True
    l = height(root.left)
    r = height(root.right)
    if r-l>1 or l-r>1:
        return False

    isLeftBalance = isBalance(root.left)
    isRightBalance = isBalance(root.right)

    if isLeftBalance and isRightBalance:
        return True
    else:
        return False

def optimizedBalance(root):
    if root==None:
        return 0,True
    l,leftBal=optimizedBalance(root.left)
    r,rightBal=optimizedBalance(root.right)
    h = l + r + 1
    if l-r>1 or r-l>1:
        return h,False
    if leftBal and rightBal:
        return h,True
    else:
        return h,False

def diameter(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)

    ld=diameter(root.left)
    rd=diameter(root.right)

    return max(lh+rh+1,max(ld,rd))

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

def printLevelWise(root):
    if root.data==-1:
        return None
    print("Root Data",root.data)
    q=queue.Queue()
    q.put(root)
    while(not(q.empty())):
        r=q.get()
        if(r.left!=None):
            print("Left child of-",r.data,"-",r.left.data)
            q.put(r.left)
        if(r.right!=None):
            print("Right child of-",r.data,"-",r.right.data)
            q.put(r.right)

    return root

#root = treeInput()
#printDetailedTree(root)

root = levelWiseInput()

print()
print("Preorder")
preOrder(root)
print()
print("Postorder")
postOrder(root)
print()
print("Inorder")
inOrder(root)
print()
#print("Largest Element-"+str(largetData(root)))
#print("Height - "+str(height(root)))
#print("Leaf Nodes - "+str(leafNodes(root)))
#print()
#print("At K Nodes")
#atKNodes(root,2)

#root = removeLeaves(root)
#print(preOrder(root))

print(isBalance(root))
print(optimizedBalance(root))

print(printLevelWise(root))