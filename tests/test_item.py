"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone



def test_calculate_total_price():
    item1 = Item("Товар 1", 10.0, 5)
    item2 = Item("Товар 2", 20.0, 3)

    assert item1.calculate_total_price() == 50.0
    assert item2.calculate_total_price() == 60.0


def test_apply_discount():
    Item.pay_rate = 0.85

    item1 = Item("Товар 1", 10.0, 5)
    item2 = Item("Товар 2", 20.0, 3)

    item1.apply_discount()
    assert item1.price == 8.5

    item2.apply_discount()
    assert item2.price == 17.0


def test_apply_discount_with_multiple_items():
    Item.pay_rate = 0.9

    item1 = Item("Товар 1", 10.0, 5)
    item2 = Item("Товар 2", 20.0, 3)
    item3 = Item("Товар 3", 30.0, 2)
    item4 = Item("Товар 4", 15.0, 4)

    item1.apply_discount()
    item2.apply_discount()
    item3.apply_discount()
    item4.apply_discount()

    assert item1.price == 9.0
    assert item2.price == 18.0
    assert item3.price == 27.0
    assert item4.price == 13.5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # Create objects from the CSV file
    assert len(Item.all) == 5  # Expecting 5 items from the file

    # Verify the names of the items
    expected_names = ['Смартфон', 'Ноутбук', 'Кабель', 'Мышка', 'Клавиатура']
    for i, item in enumerate(Item.all):
        assert item.name == expected_names[i]

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_item_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_item_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

def test_item_addition_with_item():
    item1 = Item("Smartphone", 10000, 20)
    item2 = Item("Tablet", 5000, 15)

    result = item1 + item2
    assert result == 35

def test_item_addition_with_phone():
    item1 = Item("Smartphone", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    result = item1 + phone1
    assert result == 25