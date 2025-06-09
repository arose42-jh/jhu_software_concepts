import pytest
from pizzaorders.pizza import Pizza

#mark all as pizza
pytestmark = pytest.mark.pizza

@pytest.fixture
def basicpizza():
    pizza = Pizza('thin', ['pesto'], 'Mozzarella', ['mushrooms'])
    return pizza

def what_is_a_pizza(basicpizza):
    assert True if basicpizza else False
    assert type(basicpizza[1]) == str
    assert type(basicpizza[2]) == list
    assert type(basicpizza[2][0]) == str
    assert basicpizza[3] == 'Mozzarella'
    assert type(basicpizza[4]) == list
    assert basicpizza.cost > 0 

def say_the_pizza(basicpizza):
    pizzastring = str(basicpizza)
    assert "thin" in pizzastring
    assert 'pesto' in pizzastring
    assert 'Mozzarella' in pizzastring
    assert 'mushrooms' in pizzastring
    assert '11' in pizzastring

#Make more pizzas for calculator
def cost_calculator(basicpizza):
    nocoupon = basicpizza.cost 
    assert nocoupon == 11
