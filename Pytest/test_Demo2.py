# In Pytest you cannot have multiple method name same otherwise it will override previous one
# in other testing framework it will report but in pytest it will override
# Method Name should have sense in pytest
# Regular Expression -k (CreditCard) it will run only those test method which name contains CreditCard other deselected
# py.test test_Demo2.py -k CreditCard -v -s
#  1 passed, 2 deselected in 0.08s
# -k stands for method names in execution, -s logs in output -v stands for more infromation metadata
# you can run specific file with py.test <filename>


def test_first():
    msg = "Hello"
    assert msg == "Hi" , "Test Failed because strings do not match"

def test_second():
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"

def test_SecondCreditCard():
    a=4
    b=6
    assert a+2 == b, "Addition Do not match"


