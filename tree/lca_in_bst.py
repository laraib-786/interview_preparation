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
def lca(root, v1, v2):
    if v1>root.value and v2>root.value:
        return lca(root.right, v1, v2)
    elif v1<root.value and v2<root.value:
        return lca(root.left, v1, v2)
    else:
        return root
def lca0(root, v1, v2):# brief of lca but otherwise both are same
  #Enter your code here
    if (v1<=root.value and root.value <=v2) or (v2<=root.value and root.value<=v1):
        return root
    elif v1>root.value and v2>root.value:
        return lca0(root.right, v1, v2)
    elif v1<root.value and v2<root.value:
        return lca0(root.left, v1, v2)


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
#print(maxdepth(r))
print("lowest common ancestor:")
print(lca0(r,9,12))
