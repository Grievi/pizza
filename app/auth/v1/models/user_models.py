from app import db

class User:
    '''
    Class for user opeartions
    '''
    

    __table__ = 'user'
    user_id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.Integer)

    def __repr__(self):
        return f'User {self.username}'

class Order:

    __table__ = 'order'
    order_id =db.Column(db.Integer,primary_key = True)
    food_order = db.Column(db.String(255))
    price = db.Column(db.Integer)

    def __repr__(self):
         f'Order {self.food_order}'


class Pizza:
    __table__ = 'pizza'
    id =db.Column(db.Integer,primary_key = True)
    pizza = db.Column(db.String(255))
    toppings = db.Column(db.Integer)

    def __repr__(self):
        return f'Pizza {self.pizza}'