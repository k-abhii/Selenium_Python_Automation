# Any pytest file should start with test_ or end with _test.py
# pytest method names should start with test
# Any code should be wrapped in method only
# Every test method in pytest is treated as testcase
# cmd   py.test test_demo1.py test_Demo2.py -m smoke -v -s
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_secondProgram():
    print("Good Morning")


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
# XPASS
# test_Demo2.py::test_first SKIPPED (unconditional skip)
# test_Demo2.py::test_second PASSED
# test_Demo2.py::test_SecondCreditCard PASSED
#
# ========================================================================== warnings summary ===========================================================================
# test_demo1.py:9
#   C:\Users\hp\PycharmProjects\selenium\RSA\Pytest\test_demo1.py:9: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# test_Demo2.py:18
#   C:\Users\hp\PycharmProjects\selenium\RSA\Pytest\test_Demo2.py:18: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.smoke
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ========================================================= 3 passed, 1 skipped, 1 xpassed, 2 warnings in 0.16s =========================================================