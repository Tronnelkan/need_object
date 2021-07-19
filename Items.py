from dataclasses import dataclass

@dataclass
class Item:
    photo_link: str
    id: int
    title: str
    description: str
    price: int


game1 = Item(id=1, title='Call_of_Duty_black_ops', description='Безупречная игра', price=1, photo_link='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-7FwZ8qEE0QWESaOqByE1uViLCisJVMyokQ&usqp=CAU')
game2 = Item(id=2, title='Call_of_Duty_black_ops_2', description='Безупречная игра', price=1, photo_link='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc7RdEDZeNgOWkyXI9OPmbuoAGYnjtY6SKaw&usqp=CAU')
game3 = Item(id=3, title='Call_of_Duty_black_ops_3', description='Безупречная игра', price=1, photo_link='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-ObJGNxvn_9QR3RsJ_uusljqT_D50ZFZ3CA&usqp=CAU')

items = [game1, game2, game3]