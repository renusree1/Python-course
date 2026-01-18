class comp:
    def __init__(self):
        self.__maxprice = 1000
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c=comp()
c.sell()

c.setMaxPrice(2000)
c.sell()
