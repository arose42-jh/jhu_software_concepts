import pytest
from pizzaorders.pizza import Pizza

@pytest.fixture
def basicpizza():
    pizza = Pizza('thin', ['pesto', 'marinara'], 'mozzarella', ['mushrooms'])
    return pizza

@pytest.mark.pizza
def test_what_is_a_pizza(basicpizza):
    assert True if basicpizza else False
    assert type(basicpizza.crust) == str
    assert type(basicpizza.sauce) == list
    assert type(basicpizza.sauce[0]) == str
    assert basicpizza.cheese == 'mozzarella'
    assert type(basicpizza.toppings) == list
    assert basicpizza.cost() != 0 

@pytest.mark.pizza
def test_say_the_pizza(basicpizza):
    pizzastring = basicpizza.__str__()
    assert "thin" in pizzastring
    assert 'pesto' in pizzastring
    assert 'mozzarella' in pizzastring
    assert 'mushrooms' in pizzastring
    assert '13' in pizzastring

@pytest.mark.pizza
#Make more pizzas for calculator
def test_cost_calculator(basicpizza):
    nocoupon = basicpizza.cost() 
    assert nocoupon == 13
