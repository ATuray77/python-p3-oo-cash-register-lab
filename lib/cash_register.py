#!/usr/bin/env python3

# class CashRegister:

#   def __init__(self):
#      self.discount_per = 0
#      self.total_price = 0
#      self.items = []
#      self.last_transaction = 0

#   def add_item(self, name, quantity, price):
#      item = {"name": name, "quantity": quantity, "price": price}
#      self.items.append(item)
#       #update total_price
#      self.total_price += quantity * price
     

#   def apply_discount(self, discount):
#      self.discount_per = discount

#   def calculate_total(self):
#      discount_amount = (self.discount_per/100) * self.total_price
#      return self.total_price - discount_amount
  
#   def show_items(self):
#       for item in self.items:
#          print(f"Item name: {item['name']}, Quantity: {item['quantity']}, Price per unit: {item['price']}")

#   def void_last_transaction(self):
#       if self.items:
#          last_item = self.item.pop()
#          #update total price
#          self.total_price -= last_item['quantity'] * last_item['price']
#       else: 
#          print("No transaction to void")
        



class CashRegister:
    

    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity = 1):
        for i in range(quantity):
            self.items.append(title)

        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = round(self.total - (self.total * (self.discount / 100)))
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction