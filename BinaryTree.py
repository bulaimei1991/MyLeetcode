# -*- coding=utf-8 -*-
'''
二叉树的遍历
1前序遍历
2中序遍历
3后序遍历
4层序遍历
5逆层序遍历
'''

class BinaryTreeNode():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


class BinaryTree():
    def __init__(self,root=None):
        self.root=root

    def preOrder(self,BinaryTree_):
        if BinaryTree_==None:
            return
        print BinaryTree_.data
        self.preOrder(BinaryTree_.left)
        self.preOrder(BinaryTree_.right)

    def inOrder(self,BinaryTree_):
        if BinaryTree_==None:
            return
        self.inOrder(BinaryTree_.left)
        print BinaryTree_.data
        self.inOrder(BinaryTree_.right)

    def postOrder(self,BinaryTree_):
        if BinaryTree_==None:
            return
        self.postOrder(BinaryTree_.left)
        self.postOrder(BinaryTree_.right)
        print BinaryTree_.data

    def layerOrder(self,BinaryTree_):
        Queue=[]
        FirstLayer=[]
        FirstLayer.append(BinaryTree_)
        Queue.append(FirstLayer)

        while Queue[-1]!=[]:
            layer_node = []
            for layer in Queue[-1]:
                if (layer.left!=None):
                    layer_node.append(layer.left)
                if (layer.right!=None):
                    layer_node.append(layer.right)
            Queue.append(layer_node)
        del Queue[-1]

        LayerQueue=[]
        for i in Queue:
            for j in i:
                print j.data
                LayerQueue.append(j)
        return LayerQueue

    def adjectivelayerOrder(self,BinaryTree_):
        Queue=[]
        FirstLayer=[]
        FirstLayer.append(BinaryTree_)
        Queue.append(FirstLayer)

        while Queue[-1]!=[]:
            layer_node = []
            for layer in Queue[-1]:
                if (layer.left!=None):
                    layer_node.append(layer.left)
                if (layer.right!=None):
                    layer_node.append(layer.right)
            Queue.append(layer_node)
        del Queue[-1]

        LayerQueue=[]
        for i in range(len(Queue)-1,-1,-1):
            for j in Queue[i]:
                print j.data
                LayerQueue.append(j)
        return LayerQueue

Inode=BinaryTreeNode(9)
Hnode=BinaryTreeNode(8)
Gnode=BinaryTreeNode(7)
Fnode=BinaryTreeNode(6)
Enode=BinaryTreeNode(5,right=Inode)
Dnode=BinaryTreeNode(4,left=Gnode,right=Hnode)
Cnode=BinaryTreeNode(3,left=Enode,right=Fnode)
Bnode=BinaryTreeNode(2,left=Dnode)
Anode=BinaryTreeNode(1,left=Bnode,right=Cnode)

Tree=BinaryTree(Anode)
print "前序遍历"
Tree.preOrder(Tree.root)
print "中序遍历"
Tree.inOrder(Tree.root)
print "后序遍历"
Tree.postOrder(Tree.root)
print "层序遍历"
Tree.layerOrder(Tree.root)
print "逆层序遍历"
Tree.adjectivelayerOrder(Tree.root)