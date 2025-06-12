class Pizza:
    """
    Represents a pizza with customizable crust, sauce, cheese, and toppings.

    Attributes:
        crust (str): The type of crust (e.g., 'thin', 'thick', etc.).
        sauce (list[str]): List of sauces on the pizza.
        cheese (str): The type of cheese used.
        toppings (list[str]): List of toppings on the pizza.
    """

    #initialize teh pizza with all the fixins
    crust: str
    sauce: list[str]
    cheese: str
    toppings: list[str]

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a Pizza object with crust, sauce, cheese, and toppings.

        Args:
            crust (str): The type of crust.
            sauce (list[str]): List of sauces.
            cheese (str): The type of cheese.
            toppings (list[str]): List of toppings.
        """
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    #returns string output of pizza
    def __str__(self):
        """
        Return a string representation of the pizza, including its ingredients and cost.

        Returns:
            str: Description of the pizza.
        """
        return(f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost()}")
    
    #calculates cost
    def cost(self):
        """
        Calculate the total cost of the pizza based on its ingredients.

        Returns:
            int: The total cost of the pizza.
        """
        total = 0
        if self.crust == 'thin':
            total += 5
        elif self.crust == 'thick':
            total += 6
        else:
            total += 8
        for sauce in self.sauce:
            if sauce == 'marinara':
                total += 2
            if sauce == 'pesto':
                total += 3
            if sauce == 'liv sauce':
                total +=5
        for topping in self.toppings:
            if topping == 'pineapple':
                total += 1
            elif topping == 'peperoni':
                total += 2
            else:
                total += 3
        return total
