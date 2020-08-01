""" Reference:--https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/"""

class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.value)

def insert0(root,node):
    current_node=root
    if node.value < root.value:
        if root.left==None:
            root.left=node
        else:
            current_node=current_node.left
            insert0(current_node,node)
    else:
        if root.right==None:
            root.right=node
        else:
            current_node=current_node.right
            insert0(current_node,node)
def insert(root,node):
    #if root is None:
        #root=node
    #else:
        if node.value < root.value:
            if root.left==None:
                root.left=node
            else:
                insert(root.left,node)
        else:
            if root.right==None:
                root.right=node
            else:
                insert(root.right,node)
def maxdepth(root):#each time getHeight will give height of node (leftc/rightc/root) where node can be seen as a root.
    if root==None:
        return -1
    else:#just mimic the tree and assign no to left and right child according to depth at each level .
        lDepth=maxdepth(root.right)
        rDepth=maxdepth(root.left)
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
def getHeight(root):#each time getHeight will give height of node (leftc/rightc/root) where node can be seen as a root.
        if root == None:
            return -1
        else:
            return 1 + max(getHeight(root.left), getHeight(root.right))#just mimic the tree and assign no to left and right child according to depth at each level .

def level(root,key):
    level=0
    while(root.value!=key):
        if key<root.value:
            root=root.left
            level+=1
        elif key>root.value:
            root=root.right
            level+=1
    return level

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80


#            8
#         /    \
#       6      11
#     /  \    /    \
#    5    7  10    12
#           /        \
#          9          13

"""r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))"""

r = Node(8)
insert(r,Node(6))
insert(r,Node(5))
insert(r,Node(7))
insert(r,Node(11))
insert(r,Node(12))
insert(r,Node(13))
insert(r,Node(10))
insert(r,Node(9))

# Print inoder traversal of the BST
inorder(r)
print("max_height")
print(maxdepth(r))
print(level(r,10))
