class Pizza:
    
    def __init__(self, crust, sauce, cheese, toppings):
        self.crust = crust
        self.sauce = [sauce]
        self.cheese = cheese
        self.toppings = [toppings]


    def __str__(self):
        return(f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self.cost()}")
    

    def cost(self):
        self.cost = 0
        if self.crust == 'thin':
            self.cost += 5
        elif self.crust == 'thick':
            self.cost += 6
        else:
            self.cost += 8
        for sauce in self.sauce:
            if sauce == 'marinara':
                self.cost += 2
            if sauce == 'pesto':
                self.cost += 3
            if sauce == 'liv sauce':
                self.cost +=5
        for topping in self.toppings:
            if topping == 'pineapple':
                self.cost += 1
            elif topping == 'peperoni':
                self.cost += 2
            else:
                self.cost += 3
        return self.cost
