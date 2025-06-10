class Pizza:
    #initialize teh pizza with all the fixins
    crust: str
    sauce: list[str]
    cheese: str
    toppings: list[str]

    def __init__(self, crust, sauce, cheese, toppings):
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings

    #returns string output of pizza
    def __str__(self):
        return(f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost()}")
    
    #calculates cost
    def cost(self):
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
