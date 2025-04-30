class TreeNode:
    def __init__(self,elem):
        self.elem = elem
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def tree_creation_array(self, arr, i):
        node = TreeNode(arr[i])
        node.left = self.tree_creation_array(arr, 2*i)
        node.right = self.tree_creation_array(arr, (2*i)+1)
        return node
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.elem, end =" ")
        self.inorder(root.right)
    
    def preorder(self, root):
        if root == None:
            return 
        print(root.elem, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.elem, end=" ")

    def height(self, root):
        if root == None:
            return -1
        l=self.height(root.left)
        r=self.height(root.right)
        if l > r :
            return l+1
        else:
            return r+1

    def depth(self, root, target, depth):
        if root == None:
            return -1
        if root.elem == target:
            return depth
        leftDepth = self.depth(root.left, target, depth+1)
        if leftDepth != -1:
            return leftDepth
        rightDepth = self.depth(root.right, target, depth+1)
        return rightDepth
    
    
        
