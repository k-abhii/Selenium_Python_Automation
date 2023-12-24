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

