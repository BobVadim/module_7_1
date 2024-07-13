from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return f'{self.__file_name}'

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        for Product in products:
            if Product.name not in current_products:
                file.write(str(Product) + '\n')
                current_products += str(Product) + '\n'
            else:
                print(f'Продукт {Product.name} уже есть в магазине')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
#s1.get_products()
s1.add(p1, p2, p3)
