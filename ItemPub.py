import decimal


"""
Object representing an item, contains a Name, Category, Price, nad unit of measure

clean_price is used because floats don't play nice and need to be exact for prices.
"""


class ItemPub:
    def __init__(self, name: str, category: str, price: decimal, uom: str):
        self.name = name
        self.category = category
        self.price = str(round(price, 2))
        self.uom = uom
        # int that will know when to reset the loop
        self.loop_num = 4

    # prints the data in the class for a test
    def print_for_test(self):
        print(self.name, '  ', self.category,  '  ',
              self.price, '  ', self.uom, '\n')

    # cleans the price so it can be entered properly
    def clean_price(self):
        if self.price.count('.') == 0:
            self.price += '.00'
        else:
            # find the index of the dot, and if the price doesnt go past its bad
            idx = self.price.find('.')
            if len(self.price[idx:]) < 3:
                self.price += '0'
