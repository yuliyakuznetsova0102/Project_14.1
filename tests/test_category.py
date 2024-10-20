
def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert len(first_category.list_product) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
