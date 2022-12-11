from day8 import *
def testIsBorderTree():
    testTree = Tree(0,0,3)
    isBorderTree(testTree, 5,5)
    assert testTree.isOnBorder == True

def testTreeRowChecker():
    testTreePassing = Tree(2,2,3)
    assert treeRowChecker(testTreePassing) == True
    testTreeFailing = Tree(1,2,5)
    assert treeRowChecker(testTreeFailing) == False

def testTreeColumnChecker():
    testTreePassing = Tree(1,2,5)
    assert treeColumnChecker(testTreePassing) == True
    testTreeFailing = Tree(0,2,6)
    assert treeColumnChecker(testTreeFailing) == False

if __name__ == "__main__":
    testIsBorderTree()
    testTreeRowChecker()
    testTreeColumnChecker()
    print("Everything passed")