def checkBST(root):
    n_root=root
    def check(n_node,root):
        if root==None:
            return True
        if root.left.data<root.data and root.right.data>root.data:
            if n_node!=root:
                if ((root.left.data<n_node.data and root.right.data<n_node.data) or (root.left.data>n_node.data and root.right.data>n_node.data)) :
                    return check(n_node,root.left) and check(n_node,root.right)
                else:
                    return False
            else:
                return check(n_node,root.left) and check(n_node,root.right)
boolean checkBST(root, minValue, maxValue):
    if root == None:
        return True

    if (root.data < minValue or root.data > maxValue):
        return False

    return  checkBST(root.left, minValue, root.data - 1)
            and checkBST(root.right, root.data + 1, maxValue)


boolean checkBST(root):
    return checkBST(root, 0, 10000)
