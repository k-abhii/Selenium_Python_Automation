import pytest
# prerequisite method will be executed before yield --invoke the browser --invoke some configuration
# post test execution will happen after yield --close the browser --delete the cookies
# in what scenario you add fixtures to conftest.py file when that particular fixture is shared by multiple files.
# fixtures are used as setup and teardown methods for test cases - conftest file to generalize fixture
# and make it available to all testcases
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")








#
# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_fixturesDemo.py::test_fixtureDemo I will be executing first
# PASSED                            [100%]I will execute steps in fixtureDemo method
#
#
# ============================== 1 passed in 0.04s ==============================
#
# Process finished with exit code 0


# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_fixturesDemo.py::test_fixtureDemo I will be executing first
# PASSED                            [100%]I will execute steps in fixtureDemo method
# I will be executed last
#
#
# ============================== 1 passed in 0.07s ==============================


# ============================= test session starts =============================
# collecting ... collected 4 items
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo I will be executing first
# PASSED               [ 25%]I will execute steps in fixtureDemo method
# I will be executed last
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo1 I will be executing first
# PASSED              [ 50%]I will execute steps in fixtureDemo1 method
# I will be executed last
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo2 I will be executing first
# PASSED              [ 75%]I will execute steps in fixtureDemo2 method
# I will be executed last
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo3 I will be executing first
# PASSED              [100%]I will execute steps in fixtureDemo3 method
# I will be executed last
#
#
# ============================== 4 passed in 0.31s ==============================

# ==========scope = "class"==========
# ============================= test session starts =============================
# collecting ... collected 4 items
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo I will be executing first
# PASSED               [ 25%]I will execute steps in fixtureDemo method
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo1 PASSED              [ 50%]I will execute steps in fixtureDemo1 method
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo2 PASSED              [ 75%]I will execute steps in fixtureDemo2 method
#
# test_fixturesDemo.py::TestExample::test_fixtureDemo3 PASSED              [100%]I will execute steps in fixtureDemo3 method
# I will be executed last
#
#
# ============================== 4 passed in 0.28s ==============================


