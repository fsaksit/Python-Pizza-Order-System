import csv
import datetime
#The menu.txt file is created by this code block.(Lines 4 to 22)
with open("menu.txt", "w") as menu:
    menu.write("""* Please select a pizza base:
1: Classic --->  10$
2: Margarita --->  15$
3: Turk Pizza --->  20$
4: Simple Pizza --->  7$
* Selectable Additional Materials:
11: Olive --->  2$
12: Mushroom --->  2$
13: Goat Cheese --->  5$
14: Meat --->  8$
15: Onion --->  2$
16:  Sweet Corn --->  2$
* Pizza Sizes:
S: Small --->  Standard
M: Medium --->  5$
L:Large --->  7$
* Thank you!
""")

#superclass (class Pizza)
class Pizza:
    def __init__(self):
        self.description = ""
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

#subclass (lines 37 to 74)
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza: Mozarella Cheese, Pizza Sauce, Sausage"
        self.cost = 10

    def get_cost(self):
        return self.cost


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza: Mozarella Cheese, Basil, Tomato Sauce"
        self.cost = 15

    def get_cost(self):
        return self.cost


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza: Goat Cheese, Sausage, Bacon, Pizza Sauce"
        self.cost = 20

    def get_cost(self):
        return self.cost


class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Simple Pizza: Mozarella Cheese, Pizza Sauce"
        self.cost = 7

    def get_cost(self):
        return self.cost

#superclass( Decorator Pizza)
class Decorator(Pizza):

    def __init__(self, component):
        self.component = component

    def get_description(self):
        return self.component.get_description()

    def get_cost(self):
        return self.component.get_cost()

#subclass (lines 89 to 203)
class Zeytin(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Olive"
        self.cost = 2

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class Mantar(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Mushroom"
        self.cost = 2

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class KeçiPeyniri(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Goat Cheese"
        self.cost = 5

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class Et(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Meat"
        self.cost = 8

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class Soğan(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Onion"
        self.cost = 2

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class Mısır(Decorator):
    def __init__(self, component):
        Decorator.__init__(self, component)
        self.description = "Sweet Corn"
        self.cost = 2

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class SmallPizza(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Size: Small"
        self.cost = 0

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class MediumPizza(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Size: Medium"
        self.cost = 5

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost


class LargePizza(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Size: Large"
        self.cost = 7

    def get_description(self):
        return self.component.get_description() + " , " + self.description

    def get_cost(self):
        return self.component.get_cost() + self.cost

#user payment and address information
def payment():
    global name
    name = ""
    while name == "":
        name = input("Enter Your Name : ")
        if name == "":
            print("Name cannot be left blank! ")

    global address
    address = ""
    while len(address) == 0:
        address = input('Enter Your Address: ')
        if len(address) == 0:
            print('Address cannot be left blank!')
            address = ""

    global ID
    ID = ""
    while ID == "":
        ID = input("Enter Your ID Number: ")
        if ID == "":
            print("ID number cannot be left blank! ")
        elif not ID.isdigit() or len(ID) != 11:
            print("ID number must be 11 digits and consist of numbers only!!")
            ID = ""

    global credit_card
    credit_card = ""
    while credit_card == "":
        credit_card = input("Enter Your Credit Card Number: ")
        if credit_card == "":
            print("Enter Your Credit Card Number!")
        elif not credit_card.isdigit() or len(credit_card) != 16:
            print("Credit card number must be 16 digits!")
            credit_card = ""

    global card_password
    card_password = ""
    while card_password == "":
        card_password = input("Enter Your Credit Card Password: ")

        if card_password == "":
            print("Credit card password cannot be left blank! Please Enter!")
        elif not card_password.isdigit() or len(card_password) != 4:
            print("Password must be 4 digits!")
            card_password = ""
    global card_cvv
    card_cvv = ""
    while card_cvv == "":
        card_cvv = input("Enter Credit Card CVV Number : ")

        if card_cvv == "":
            print("Credit Card CVV cannot be blank!Please Enter!")
        elif not card_cvv.isdigit() or len(card_cvv) != 3:
            print("Credit Card CVV number must be 3 digits!")
            card_cvv = ""

#selection part
def main():
    baslık = "Welcome to Pizza Order System"
    print(baslık.center(25))
    with open("menu.txt", "r") as file:
        menu = file.read()
        print(menu)

    pizza_type = ""
    while pizza_type == "":
        pizza_type = int(input("Please Select Your Pizza: "))
        if pizza_type == 1:
            pizza = KlasikPizza()
        elif pizza_type == 2:
            pizza = MargaritaPizza()
        elif pizza_type == 3:
            pizza = TurkPizza()
        elif pizza_type == 4:
            pizza = SadePizza()
        else:
            print("Invalid Choice!")
            pizza_type = ""

    while True:
        topping_type = int(input(
            "Please select additional materials!(Press 0 to switch to pizza size selection!): "))
        if topping_type == 0:
            break
        elif topping_type == 11:
            pizza = Zeytin(pizza)
        elif topping_type == 12:
            pizza = Mantar(pizza)
        elif topping_type == 13:
            pizza = KeçiPeyniri(pizza)
        elif topping_type == 14:
            pizza = Et(pizza)
        elif topping_type == 15:
            pizza = Soğan(pizza)
        elif topping_type == 16:
            pizza = Mısır(pizza)
        else:
            print("Invalid Choice!")

    while True:
        topping_type = input("Please Select A Size: ")
        if topping_type == "q":
            break
        elif topping_type == "S":
            pizza = SmallPizza(pizza)
            break
        elif topping_type == "M":
            pizza = MediumPizza(pizza)
            break
        elif topping_type == "L":
            pizza = LargePizza(pizza)
            break
        else:
            print("Invalid Choice!")

    payment()
#user payment and address information and write to Orders_Database.csv 
    time_order = datetime.datetime.now()
    with open('Orders_Database.csv', 'a', encoding="utf-8") as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, address, credit_card, card_cvv,
                        card_password, pizza.get_description(), time_order])

#here is for print total price and order information 
    print("--------------Order Infromation-----------------")
    print("", name.title(), "\n", address.title(), "\n", pizza.get_description(
    ), "\nTotal Price: " + "", str(pizza.get_cost()), "$", "\n", time_order)


if __name__ == "__main__":
    main()

#ozberkayada10@gmail.com
#fatihsaksit@gmail.com
#amedturkan@hotmail.com