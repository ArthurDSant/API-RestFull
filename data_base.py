from enum import Enum
from pydantic import BaseModel

class Category(Enum):
    HARDWARE = 'hardware'
    PERIPHERALS = 'peripherals'
    SOFTWARE = 'software'

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

items = {
    0: Item(name='Ethernet Cable', price=4.99, count=150, id=0, category=Category.HARDWARE),
    1: Item(name='Wireless Adapter', price=29.99, count=50, id=1, category=Category.HARDWARE),
    2: Item(name='Surge Protector', price=19.99, count=75, id=2, category=Category.HARDWARE),
    3: Item(name='Mouse', price=29.99, count=50, id=3, category=Category.PERIPHERALS),
    4: Item(name='Keyboard', price=49.99, count=30, id=4, category=Category.PERIPHERALS),
    5: Item(name='Monitor', price=199.99, count=15, id=5, category=Category.HARDWARE),
    6: Item(name='USB Flash Drive', price=14.99, count=80, id=6, category=Category.HARDWARE),
    7: Item(name='External Hard Drive', price=89.99, count=25, id=7, category=Category.HARDWARE),
    8: Item(name='RAM 16GB', price=79.99, count=40, id=8, category=Category.HARDWARE),
    9: Item(name='SSD 1TB', price=109.99, count=35, id=9, category=Category.HARDWARE),
    10: Item(name='Graphics Card', price=299.99, count=10, id=10, category=Category.HARDWARE),
    11: Item(name='Power Supply 600W', price=59.99, count=25, id=11, category=Category.HARDWARE),
    12: Item(name='Antivirus Software', price=39.99, count=60, id=12, category=Category.SOFTWARE),
    13: Item(name='Office Suite License', price=99.99, count=50, id=13, category=Category.SOFTWARE),
    14: Item(name='Laptop Cooling Pad', price=19.99, count=40, id=14, category=Category.PERIPHERALS),
    15: Item(name='HDMI Cable', price=7.99, count=100, id=15, category=Category.HARDWARE),
}