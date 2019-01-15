from threading import Lock


class BankAccount(object):
    """Simple bank account implementation"""

    def __init__(self):
        self.is_open = False
        self.lock = Lock()

    def with_open_account(func):
        """Decorator throwing an exception if account is closed"""

        def wrapper_with_open_account(self, *args, **kwargs):
            if not self.is_open:
                raise ValueError('Account is closed!')
            return func(self, *args, **kwargs)
        return wrapper_with_open_account

    def with_lock(func):
        """Decorator performing thread's locking on function"""

        def wrapper_with_lock(self, *args, **kwargs):
            with self.lock:
                return func(self, *args, **kwargs)
        return wrapper_with_lock

    @with_open_account
    def get_balance(self):
        return self.balance

    @with_lock
    def open(self):
        if self.is_open:
            raise ValueError('Account already opened!')

        self.is_open = True
        self.balance = 0

    @with_open_account
    @with_lock
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Cannot deposit negative amount!')

        self.balance += amount

    @with_open_account
    @with_lock
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Cannot withdraw more than current balance!')
        if amount < 0:
            raise ValueError('Cannot withdraw negative amount!')

        self.balance -= amount

    @with_open_account
    @with_lock
    def close(self):
        self.is_open = False
