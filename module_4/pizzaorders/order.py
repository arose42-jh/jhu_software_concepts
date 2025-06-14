from .pizza import Pizza
class Order:
    """
    Represents a customer's order, containing multiple pizzas, total cost, and payment status.

    Attributes:
        pizzas (list[Pizza]): List of Pizza objects in the order.
        cost (int): Total cost of the order.
        is_paid (bool): Payment status of the order.
    """
    def __init__(self):
        """
        Initialize a new customer order with no pizzas, zero cost, and unpaid status.
        """
    #Initializes a customer order
    #Initializes order cost
    #Sets order as unpaid
        self.pizzas = []
        self.cost = 0
        self.is_paid = False
        return

    def __str__(self):
        """
        Return a string representation of the complete customer order, listing all pizzas.

        Returns:
            str: Description of the order and its pizzas.
        """
        #return a customers complete order
        lines = ["Customer Requested:"]
        #Account for multiple pizzas
        for  pizza in self.pizzas:
            lines.append(f"{pizza}")
        return "\n".join(lines)    
        
    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Add a pizza to the order with the specified ingredients and update the total cost.

        Args:
            crust (str): The type of crust.
            sauce (list[str]): List of sauces.
            cheese (str): The type of cheese.
            toppings (list[str]): List of toppings.
        """
        #input the customers order for a given pizza
        #initialize the pizza object and attach to the order
        #update the cost
        newpizza = Pizza(crust,sauce,cheese,toppings)
        self.pizzas.append(newpizza)
        self.cost += newpizza.cost()
        return
    
    def order_paid(self):
        """
        Mark the order as paid.
        """
        #Set order as paid once payment has been collected
        self.is_paid = True
        return
