import pytest
from src.order import Order

#Using fixtures to set up test cases for the tests to come
@pytest.fixture
def empty_order():
    return Order()

#Start of order tests
#initialization tests
@pytest.mark.order
def test_starts_empty(empty_order):
    assert len(empty_order.pizzas) == 0
    assert empty_order.cost == 0
    assert empty_order.is_paid is False

#Input pizza tests, this second because other functions depend on it (i know it tests out of order)
@pytest.mark.order
@pytest.mark.pizza
def test_two_pizza(empty_order):
    empty_order.input_pizza('gf', ['liv sauce'], 'mozz', ['mushrooms pineapple'])
    cost1 = empty_order.cost
    empty_order.input_pizza('thick', ['liv sauce'], 'mozz', ['peperoni'])
    assert empty_order.cost > 0
    assert empty_order.cost > cost1
    assert empty_order.is_paid is False
    assert len(empty_order.pizzas) == 2

@pytest.mark.pizza
@pytest.mark.order
def test_multi_sacuce_toppings(empty_order):
    empty_order.input_pizza('thin', ['liv sauce', 'pesto'], 'Mozzarella', ['pineapple', 'mushrooms'])
    assert len(empty_order.pizzas) == 1
    assert empty_order.cost > 0


#Output String tests
@pytest.mark.pizza
@pytest.mark.order
def test_str_with_onepizza(empty_order):
    empty_order.input_pizza('thin', ['liv sauce', 'pesto'], 'mozz', ['pineapple'])
    orderstring = str(empty_order)
    assert 'Customer Requested:' in orderstring
    assert 'Cost: ' in orderstring
    assert 'Cost: $0.00' not in orderstring

#paid tests
@pytest.mark.order
def test_paid(empty_order):
    empty_order.order_paid()
    assert empty_order.is_paid is True