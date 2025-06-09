import pytest
from pizzaorders.order import Order

#Using fixtures to set up test cases for the tests to come
@pytest.fixture
def empty_order():
    return Order()

@pytest.fixture
def one_pizza():
    order = Order()
    order.input_pizza('thin', 'liv sauce', 'mozz', 'pineapple')
    return order

@pytest.fixture
def two_pizza():
    #includes 2 pizzas and multiple toppings
    order = Order()
    order.input_pizza('gf', 'liv sauce', 'mozz', 'mushrooms pineapple')
    order.input_pizza('thick', 'liv sauce', 'mozz', 'peperoni')
    return order

@pytest.fixture
def paid_pizza():
    order = Order()
    order.input_pizza('thin', 'liv sauce', 'mozz', 'pineapple')
    order.order_paid()
    return order

#Start of order tests
#initialization tests
def test_starts_empty(empty_order):
    assert len(empty_order.pizzas) == 0
    assert empty_order.total_cost == 0.0
    assert empty_order.is_paid is False

def empty_order_string(empty_order):
    output = 'Order: \nPizzas ordered: \n Cost: $0.00'
    assert (str(empty_order)) == output

#Input pizza tests, this second because other functions depend on it (i know it tests out of order)
def test_add_pizza(empty_order):
    empty_order.input_pizza('gf', 'Marinara', 'Mozzarella', 'Pineapple')
    assert len(empty_order.pizzas) == 1
    assert empty_order.cost > 0
    assert empty_order.is_paid is False

def test_two_pizza(empty_order):
    empty_order.input_pizza('gf', 'liv sauce', 'mozz', 'mushrooms pineapple')
    empty_order.input_pizza('thick', 'liv sauce', 'mozz', 'peperoni')

    assert len(empty_order.pizzas) == 2

def test_multi_sacuce_toppings(empty_order):
    empty_order.input_pizza('thin', ['liv sauce', 'pesto'], 'Mozzarella', ['pineapple', 'mushrooms'])
    assert len(empty_order.pizzas) == 1
    assert empty_order.cost > 0

#Output String tests
def str_with_onepizza(one_pizza):
    orderstring = str(one_pizza)
    assert 'Order: ' in orderstring
    assert 'Pizzas ordered: ' in orderstring
    assert 'Pizza 1: ' in orderstring
    assert 'Pizza 2' not in orderstring
    assert 'Cost: ' in orderstring
    assert 'Cost: $0.00' not in orderstring

def str_with_twopizzas(two_pizza):
    orderstring = str(two_pizza)
    assert 'Order: ' in orderstring
    assert 'Pizzas ordered: ' in orderstring
    assert 'Pizza 1: ' in orderstring
    assert 'Pizza 2' in orderstring
    assert 'Cost: ' in orderstring
    assert 'Cost: $0.00' not in orderstring

#paid tests
def order_notpaid(one_pizza):
    assert one_pizza.is_paid is False

def ordercanbe(paid_pizza):
    assert paid_pizza.is_paid is True