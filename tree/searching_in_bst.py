#Why i am not getting True or False instead of  None If i am callng print(search0(root,47) )this is searching a key in BST.
class Node:
    def __init__(self,key):
        self.value=key
        self.left=None
        self.right=None
def insert(root,node):
    if root is None:
        root=node
    else:
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
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)

        inorder(root.right)
def search0(root,key):
    if root is None:
        return False
    if root.value>key:
        return search0(root.left,key)
    elif root.value<key:
        return search0(root.right,key)
    else:
        return True
def search(root,key):
    while root != None:
        # pass right subtree as new tree
        if key > root.value:
            root = root.right
        # pass left subtree as new tree
        elif key < root.value:
            root = root.left
        else:
            return True # if the key is found return 1
    return False


def search1(root,key):

    # Base Cases: root is null or key is present at root
    if root is None or root.value == key:
        return root # equal to None if root is None means key is not present

    # Key is greater than root's key
    if root.value < key:
        return search1(root.right,key)

    # Key is smaller than root's key
    return search1(root.left,key)


# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
inorder(r)
print(search0(r,100))
print(search0(r,30))

#Output:
#20
#30
#40
#50
#60
#70
#80
#None
#None
