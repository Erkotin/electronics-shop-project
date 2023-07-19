from src.phone import Phone
from src.item import Item

def test_phone_creation():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test_phone_addition_with_item():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Smartphone", 10000, 20)

    result = phone1 + item1
    assert result == 25

def test_phone_addition_with_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Galaxy S21", 100_000, 3, 1)

    result = phone1 + phone2
    assert result == 8

