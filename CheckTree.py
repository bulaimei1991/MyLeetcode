'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        result = []
        result = self.preOrder(root, result)
        lenresult = len(result)
        for i in range(0, lenresult - 1):
            if result[i] >= result[i + 1]:
                return False
        return True

    def preOrder(self, TreeNode, result):
        if TreeNode == None:
            return
        self.preOrder(TreeNode.left, result)
        result.append(TreeNode.val)
        self.preOrder(TreeNode.right, result)
        return result


Inode=BinaryTreeNode(9)
Hnode=BinaryTreeNode(8)
Gnode=BinaryTreeNode(7)
Fnode=BinaryTreeNode(6)
Enode=BinaryTreeNode(5,right=Inode)
Dnode=BinaryTreeNode(4,left=Gnode,right=Hnode)
Cnode=BinaryTreeNode(3,left=Enode,right=Fnode)
Bnode=BinaryTreeNode(2,left=Dnode)
Anode=BinaryTreeNode(1,left=Bnode,right=Cnode)


result=[]

A=BinaryTreeNode()
result=A.preOrder(Anode,result)
print A.check(result)