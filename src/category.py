class Category:
    """Категория товара"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    list_product: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.list_product = products
        Category.category_count += 1
        Category.product_count += len(products)
