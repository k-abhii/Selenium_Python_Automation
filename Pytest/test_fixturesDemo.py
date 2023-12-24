import pytest
# prerequisite method will be executed before yield --invoke the browser --invoke some configuration
# post test execution will happen after yield --close the browser --delete the cookies
@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")




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
