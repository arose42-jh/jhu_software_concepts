import pytest
from src.order import Order
from src.pizza import Pizza

@pytest.fixture
def empty_order():
    return Order()

#Integration test
#Mulitple pizzas, multiple topings
@pytest.mark.order
@pytest.mark.pizza
def test_integration(empty_order):
    empty_order.input_pizza('gluten_free', ['liv sauce'], 'mozzarella', ['mushrooms pineapple'])
    cost1 = empty_order.cost
    empty_order.input_pizza('thick', ['liv sauce'], 'mozzarella', ['peperoni'])
    assert empty_order.cost > 0
    assert empty_order.cost > cost1
    assert empty_order.is_paid is False
    assert len(empty_order.pizzas) == 2