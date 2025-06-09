import pytest
from pizzaorders.pizza import Pizza

@pytest.fixture
def basicpizza():
    pizza = Pizza('thin', ['pesto'], 'Mozzarella', ['mushrooms'])
    return pizza

@pytest.mark.pizza
def what_is_a_pizza(basicpizza):
    assert True if basicpizza else False
    assert type(basicpizza.crust) == str
    assert type(basicpizza.sauce) == list
    assert type(basicpizza.sauce[0]) == str
    assert basicpizza.cheese == 'mozzarella'
    assert type(basicpizza.toppings) == list
    assert basicpizza.cost > 0 

@pytest.mark.pizza
def say_the_pizza(basicpizza):
    pizzastring = str(basicpizza)
    assert "thin" in pizzastring
    assert 'pesto' in pizzastring
    assert 'Mozzarella' in pizzastring
    assert 'mushrooms' in pizzastring
    assert '11' in pizzastring

@pytest.mark.pizza
#Make more pizzas for calculator
def cost_calculator(basicpizza):
    nocoupon = basicpizza.cost 
    assert nocoupon == 11
