class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль
    """

    def __init__(self, username, password, age):
        self.username = str(username)
        self.password = hash(password)
        self.age = int(age)
        # if password == password_confirm:
        #     self.password = hash(password)

