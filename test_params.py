import pytest


#@pytest.fixture(params=["a", "b"])
#def demo_fixture(request):
   # print(request.param)

#def test_params(demo_fixture):
   # print("Added Success")


@pytest.mark.parametrize("a, b, c, result", [(4, 5, 6, 1), (4, 5, 6, 15), (4, 5, 6, 15)])
def test_add(a, b, c, result):
    assert a + b + c == result


#def test_remove_item_from_cart(setUp):
   # print("Remove Success")