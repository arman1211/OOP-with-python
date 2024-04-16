product_list = {}
class Product:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

class Shop(Product):
    def __init__(self, name, price,quatity) -> None:
        self.quantity = quatity
        super().__init__(name, price)
    def add_product(self):
        product_list['name'] = self.name
        product_list['price'] = self.price
        product_list['quantity'] = self.quantity
    def get_product(self):
        for keys,value in product_list.items():
            print(f'{keys} : {value}')
    def buy_product(self,product_name):
        self.product_name = product_name
        if(product_name in product_list.values()):
            print('succesfully purchased')
        else:
            print('sorry')

iphone = Shop('iphone 15',125000,1)
iphone.add_product()
iphone.get_product()
iphone.buy_product('iphone 16')
