"""For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:
The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
The data value of every node is distinct.<<<<important.# SO WE TAKE root.data-1 AND root.data-1"""
class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.value)
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

def check(root, minValue, maxValue):
    if root == None:
        return True

    if (root.value <= minValue or root.value >= maxValue):
        return False

    return  check(root.left, minValue, root.value) and check(root.right, root.value, maxValue)#
def checkBST(root):
    return check(root, 0, 10000)
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

print(checkBST(r))
