from computer import *
# OR
# from computer import Computer

class ResaleShop:

    # What attributes will it need?
    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    # def buy(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int): # prob will have to pass in info about computer we're trying to buy
    #     # 1. call Computer(...) constructor 
    #     # to create a new computer instance

    #     # 2. call inventory.append() to add that
    #     # new Computer instance to inventory
    #     c = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    #     print("Buying" + description)
    #     self.inventory.append(c)

    # def sell(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int): # prob will have to pass in info about computer we're trying to buy
    #     c = Computer(description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price)
    #     print("Selling" + description)
    #     self.inventory.remove(c)

    def buy(self, c:Computer): # prob will have to pass in info about computer we're trying to buy
    #     # 1. call Computer(...) constructor 
    #     # to create a new computer instance

    #     # 2. call inventory.append() to add that
    #     # new Computer instance to inventory

        self.inventory.append(c)

    def sell(self, c:Computer):
        if c in self.inventory:
            self.inventory.remove(c)

        else:
            print("Computer is not in inventory.")

    def update_price(self, c:Computer, new_price):
        # self.price(c) = new_price 
        c.price = new_price

    # def update_OS(self, c:Computer, new_OS):
    #     c.operating_system = new_OS

    def print_inventory(self):
        if self.inventory == []:
             print("Inventory is empty.")
        else:
            print(self.inventory)

    def refurbish(self, c:Computer):
        if c in self.inventory: 
            if int(c.year_made) < 2000:
                c.price = 0
                # print("Computer is too old to sell.")
            elif int(c.year_made) < 2012: 
                c.price = 250
            elif int(c.year_made) < 2018:
                c.price = 550
            else:
                c.price = 1000
            
            # if new_OS is not None:
            #     c.operating_system = new_OS

        else:
            print("Item", c, "was not found in inventory.")


def main():
    myStore = ResaleShop()
    # print(myStore.inventory) # []

    # myStore.buy("Mac Pro (Late 2013)",
    #     "3.5 GHc 6-Core Intel Xeon E5",
    #     1024, 64,
    #     "macOS Big Sur", 2013, 1500)

    c = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    myStore.buy(c)
    print(myStore.inventory[0].description)
    myStore.buy(c)
    print(myStore.inventory[1].operating_system)
    myStore.print_inventory()

    # c2 = Computer("Mac Pro (Mid 2014))",
    #     "2.5 GHz Core i7",
    #     512, 16,
    #     "macOS Big Sur", 2014, 1600)
    # myStore.update_price(2500)
    # myStore.buy(c2)
    # print(myStore.inventory[5].price)

    # myStore.sell(c)
    # myStore.print_inventory()



main() 

# def main():
#     myStore = ResaleShop()
#     print(myStore.inventory) # []
    
    # c = Computer("Mac Pro", "M1", ...)
    # myStore.buy(c)