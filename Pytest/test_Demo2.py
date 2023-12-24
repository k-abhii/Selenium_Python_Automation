# In Pytest you cannot have multiple method name same otherwise it will override previous one
# in other testing framework it will report but in pytest it will override
# Method Name should have sense in pytest
# Regular Expression -k (CreditCard) it will run only those test method which name contains CreditCard other deselected
# py.test test_Demo2.py -k CreditCard -v -s
#  1 passed, 2 deselected in 0.08s
# -k stands for method names in execution, -s logs in output -v stands for more infromation metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests   @pytest.mark.smoke  and then run with -m
# -k is more optimised than -m use -m only to mention smoke or regression
# you can skip test with @pytest.mark.skip
import pytest


@pytest.mark.smoke
@pytest.mark.skip
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

# C:\Users\hp\PycharmProjects\selenium\RSA\Pytest>py.test test_demo1.py test_Demo2.py  -v -s
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.8.2, pytest-7.4.3, pluggy-1.3.0 -- c:\python38\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\hp\PycharmProjects\selenium\RSA\Pytest
# plugins: xdist-3.5.0
# collected 5 items
#
# test_demo1.py::test_firstProgram Hello
# PASSED
# test_demo1.py::test_secondProgram Good Morning
# PASSED
# test_Demo2.py::test_first SKIPPED (unconditional skip)
# test_Demo2.py::test_second PASSED
# test_Demo2.py::test_SecondCreditCard PASSED

# ========================================================================== warnings summary ===========================================================================
# test_demo1.py:9
#   C:\Users\hp\PycharmProjects\selenium\RSA\Pytest\test_demo1.py:9: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# test_Demo2.py:14
#   C:\Users\hp\PycharmProjects\selenium\RSA\Pytest\test_Demo2.py:14: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ============================================================== 4 passed, 1 skipped, 2 warnings in 0.18s ===============================================================

