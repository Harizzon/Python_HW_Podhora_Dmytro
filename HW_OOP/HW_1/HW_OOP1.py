class Product:

    def __init__(self, price, category, name, units):
        """

        :param price: integer
        :param category: food, household chemicals, alcohol
        :param name: string
        :param units: kilos, liter, bottles
        """
        self.price = price
        self.name = name
        self.units = units
        self.category = category

    def is_eatable(self):
        """
        This method return True if product is not a household chemicals
        :return: boolean
        """
        if self.category != "household chemicals":
            return True
        else:
            return False

    def price_total(self, amount):
        """
        This method return total price of your product
        :param amount: integer
        :return: integer
        """
        return self.price * amount

    @property
    def get_full_info(self):
        return f"You have {self.name} with price {self.price} and it's {self.category}"


class Basket:
    def __init__(self, product_list):
        self.product_list = product_list

    def get_total(self):
        """
        This method return total sum from your list
        :return: integer
        """
        sum = 0
        for x, y in self.product_list:
            sum += x.price * y
        return sum

    def totally_eatable(self):
        """
        This method can tell you is all products can be eaten
        :return: boolean
        """

        sum = 0
        for x, y in self.product_list:
            if (x.category) == "food" or x.category == "alcohol":
                sum += 1
            else:
                continue
        if sum == len(self.product_list):
            return True
        else:
            return False


def run():
    x = Product(12, 'food', 'frist prod', 'kilos')
    y = Product(13, 'alcohol', 'sec prod', 'litres')
    z = Product(14, 'household chemistry', "3d prod", "bottles")
    prod_list = [(x, 12), (y, 4), (z, 1)]
    buy = Basket([(x, 12), (y, 4), (z, 1)])
    print(buy.totally_eatable())
    print(buy.get_total())


if __name__ == '__main__':
    run()
