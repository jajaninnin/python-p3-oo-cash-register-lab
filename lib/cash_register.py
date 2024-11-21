#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transaction = {"price": 0, "quantity": 1}

  def add_item(self, name, price, quantity = 1):
    for notUsed in range(quantity):
      self.items.append(name)
    self.total += price * quantity
    self.last_transaction = {'price': price, 'quantity': quantity}

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total * ((100 - self.discount) / 100)
      print(f"After the discount, the total comes to ${float(self.total):g}.")

  def void_last_transaction(self):
      self.total -= self.last_transaction['price'] * self.last_transaction['quantity']
