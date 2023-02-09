class Computer:

    ## if you look inside main.py, you'll find a helper function used to create the dictionary containing all the info about a computer that we needed for the demo

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?


    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity 
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price



    # What methods will you need?
    def update_OS(self, new_OS): 
        self.operating_system = new_OS
        
    def update_price(self, new_price): 
        self.price = new_price 

    def print_details(self):
        print(self.description)
        print(self.operating_system)
        print(self.processor_type)
        print(self.memory)
        print(self.year_made)
        print(self.price)


def main():
    c = Computer( "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    c.print_details()
    c.update_OS("lucky")
    c.print_details()
    

if __name__ == "__main__": main()

