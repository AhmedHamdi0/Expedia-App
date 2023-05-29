from .user import Customer
from .api.payment.payment_common import DebitCard, CreditCard

class UsersManager:
    def __init__(self):
        self.username_userobject_dct = {}
        self._load_database()

    def _load_database(self):
        user = Customer('Mohammed', 'mo11', 'Mohammed Hamdi', 'mohamed@gmail.com')
        user.payment_cards.append(DebitCard('Mohammed', '1234', '09-2035', '008', 'BC@Canada'))
        user.payment_cards.append(CreditCard('Mohammed', '4321', '09-2035', '238', 'CA@USA'))
        self.username_userobject_dct[user.user_name] = user

        user = Customer("Ahmed Hamdi", "22", "ahmed@gmail.com", "Ahmed Ahmed")
        self.username_userobject_dct[user.user_name] = user

    def get_user(self, username, password):
        if username not in self.username_userobject_dct:
            return None

        user = self.username_userobject_dct[username]

        if user.password != password:
            return None

        return user


if __name__ == '__main__':
    mgr = UsersManager()
    mgr._load_database()