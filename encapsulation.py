class Product:
    def __init__(self):
        self.__maxprice = 900
        self.name = "laptop"
    def sell(self):
        print(self.__maxprice)
    def setMaxPrice(self, obj):
        self.__maxprice = obj
p = Product()

p.sell()
# print(p.__maxprice)
# p.__maxprice=1000
# p.name = "TV"
# print(p.name)
p.sell()
p.setMaxPrice(1000)
p.sell()