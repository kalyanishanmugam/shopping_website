from datetime import date
today = date.today()
format_string = "%d-%m-%Y"


class Product_List(object):
    def __init__(self, item_name, price, quantity, expiry_date):
        self.__item_name = item_name
        self.__price = price
        self.__quantity = quantity
        self.__expiry_date = expiry_date

    def show_list(self):
        print("Item:", self.__item_name, "Price:", (str(self.__price))+("€"), "Available_quantity:", self.__quantity)

    def expired_product(self):
        if self.__expiry_date == today:
            return "The item", self.__item_name, "has expired."

    def remove_item(self, amount):
        if self.__quantity > 0:
            self.__quantity = self.__quantity - amount
        return self.__quantity

    def add_item(self, amount):
        self.__quantity = self.__quantity + amount
        return self.__quantity

    def add_price(self, value):
        self.__price = self.__price + value
        return (str(self.__price))+("€")

    def reduce_price(self, value):
        self.__price = self.__price - value
        return (str(self.__price))+("€")

    def order_required(self):
        if self.__quantity < 10:
            return "Warning! The stock for ", self.__item_name, "is low"


class Customer(object):
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.items = {}
        print("Welcome", name)

    def add_item(self, item_name, quantity, price):
        self.total += price * quantity
        self.items.update({item_name: quantity})
        return "The item", item_name, "has been added to your cart"

    def remove_item(self, item_name, quantity, price):
        if item_name in self.items:
            if quantity < self.items[item_name] and quantity > 0:
                self.items[item_name] -= quantity
                self.total -= price * quantity
            elif quantity >= self.items[item_name]:
                self.total -= price * self.items[item_name]
                del self.items[item_name]
            return "The item", item_name, "has been removed from your cart"

    def show_customer_cart(self):
        return "Selected products are:", ("Item/Quantity")+(str(self.items)), "Total_cost =", str(self.total)+("€")

    def checkout(self, amount_paid):
        if amount_paid > self.total:
            print("Your paid:", str(amount_paid))
            return "Thanks for shopping with us, your balance is:", (str(amount_paid - self.total))+("€"), "Have a nice Day!"

        elif amount_paid == self.total:
            return "Balance = 0€, Thanks for shopping with us, Have a nice Day!"



product1 = Product_List("bread", 2, 7, today)
product1.remove_item(4)
product1.add_price(0.30)
print(product1.show_list())
print(product1.expired_product())
print(product1.order_required())


product2 = Product_List("Milk", 1, 12, 12-10-2021)
product2.add_item(20)
print(product2.show_list())

guest1 = Customer("Andrew")
guest1.add_item("Milk", 4, 2.00)
guest1.add_item("Butter", 1, 2.50)
print(guest1.add_item("Oranges", 2, 2.00))
print(guest1.remove_item("Milk", 1, 2.00))
print(guest1.show_customer_cart())
print(guest1.checkout(12.5))

