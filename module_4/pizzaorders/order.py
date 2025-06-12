from pizzaorders.pizza import Pizza
class Order:
    def __init__(self):
    #Initializes a customer order
    #Initializes order cost
    #Sets order as unpaid
        self.pizzas = []
        self.cost = 0
        self.is_paid = False
        return

    def __str__(self):
        #return a customers complete order
        lines = ["Customer Requested:"]
        #Account for multiple pizzas
        for  pizza in self.pizzas:
            lines.append(f"{pizza}")
        return "\n".join(lines)    
        
    def input_pizza(self, crust, sauce, cheese, toppings):
        #input the customers order for a given pizza
        #initialize the pizza object and attach to the order
        #update the cost
        newpizza = Pizza(crust,sauce,cheese,toppings)
        self.pizzas.append(newpizza)
        self.cost += newpizza.cost()
        return
    
    def order_paid(self):
        #Set order as paid once payment has been collected
        self.is_paid = True
        return
