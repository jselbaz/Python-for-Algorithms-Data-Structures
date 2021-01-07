class BinaryTree(object):
        def __init__(self, rootObj):
                self.key = rootObj
                self.leftChild = None
                self.rightChild = None
        
        def insertLeft(self, newNode):
                if self.leftChild == None:
                        self.leftChild = BinaryTree(newNode)
                t = BinaryTree(newNode)
                t.leftChild = self.leftChild
                self.leftChild = t
                
        def insertRight(self, newNode):
                if self.rightChild == None:
                        self.rightChild = BinaryTree(newNode)
                t = BinaryTree(newNode)
                t.rightChild = self.rightChild
                self.rightChild = t
        
        def getLeftChild(self):
                return self.leftChild
                
        def getRightChild(self):
                return self.rightChild
                
        def setRootVal(self, obj):
                self.key = obj
                
        def getRootVal(self):
                return self.key
                
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild().getRootVal())