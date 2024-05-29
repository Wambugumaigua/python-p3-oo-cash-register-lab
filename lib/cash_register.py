#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0
        self.discount = discount


    def add_item(self, item_cost):
        self.total += item_cost
        self.items.append(item_cost)
        self.last_transaction_amount = item_cost

