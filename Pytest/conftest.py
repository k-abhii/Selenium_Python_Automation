import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Abhimanyu","Kumar","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","Abhimanyu","Kumar"), ("Firefox","Abhimanyu"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
