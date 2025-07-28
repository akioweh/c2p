"""
1352. Product of the Last K Numbers
"""


class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]
        self.total_product = 1
        self.last_zero_index = -1

    def add(self, num: int) -> None:
        if num != 0:
            self.total_product *= num
        else:
            self.last_zero_index = len(self.prefix_product)
        self.prefix_product.append(self.total_product)

    def getProduct(self, k: int) -> int:
            # check if there is a zero in the last k numbers
            if self.last_zero_index >= len(self.prefix_product) - k:
                return 0
            return self.total_product // self.prefix_product[-k - 1]
