from src.math_operations import add,sub

def test_add():
    assert add(3,4)==7
    assert add(-1,4)==3
    assert add(-7,-3)==-10
    assert add(8,4)==12


def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(5,5)==0
    assert sub(9,1)==8
