from ktharraymapping import TreeAncestor
n=7
parent=[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
node=8
k=1
obj = TreeAncestor(n, parent)
def test_ans():
    
    # param_1 = obj.getKthAncestor(node,k)
    assert obj.getKthAncestor(7,1)==3
    # assert obj.getKthAncestor(7,1)==3
    # assert obj.getKthAncestor(9,1)==4
    # assert obj.getKthAncestor(9,2)==1
    # #second round
    # assert obj.getKthAncestor(2,1)==0
    # assert obj.getKthAncestor(10,1)==4
    # assert obj.getKthAncestor(11,1)==5
    # assert obj.getKthAncestor(11,2)==2
def test2():
    assert obj.getKthAncestor(7,1)==3
def test3():
    assert obj.getKthAncestor(11,2)==2
def test4():
    assert obj.getKthAncestor(11,1)==5
def test5():
    assert obj.getKthAncestor(9,2)==1
def test6():
    assert obj.getKthAncestor(9,1)==4
def test7():
    assert obj.getKthAncestor(9,2)==1