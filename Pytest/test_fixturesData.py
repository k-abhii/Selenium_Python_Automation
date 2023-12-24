import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])
        print(dataLoad[2])


# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_fixturesData.py::TestExample2::test_editProfile user profile data is being created
# PASSED              [100%]['Abhimanyu', 'Kumar', 'rahulshettyacademy.com']
#
#
# ============================== 1 passed in 0.06s ==============================

# ============================= test session starts =============================
# collecting ... collected 1 item
#
# test_fixturesData.py::TestExample2::test_editProfile user profile data is being created
# PASSED              [100%]['Abhimanyu', 'Kumar', 'rahulshettyacademy.com']
# Abhimanyu
# Kumar
# rahulshettyacademy.com

#
# collecting ... collected 5 items
#
# test_demo1.py::test_firstProgram PASSED                                  [ 20%]Hello
#
# test_demo1.py::test_secondProgram XPASS                                  [ 40%]Good Morning
#
# test_demo1.py::test_crossBrowser[crossBrowser0] PASSED                   [ 60%]Abhimanyu
#
# test_demo1.py::test_crossBrowser[crossBrowser1] PASSED                   [ 80%]Abhimanyu
#
# test_demo1.py::test_crossBrowser[crossBrowser2] PASSED                   [100%]SS
#
#
# =================== 4 passed, 1 xpassed, 1 warning in 0.12s ===================


