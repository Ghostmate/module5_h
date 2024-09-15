# import database
# import users

# from database import Database
# from users import User
from urtube import UrTube
from video import Video

# if __name__ == '__main__':
#     database = Database()
#     while True:
#         choice = input("Приветствую! Выберите действие:\n"
#                        "1 - Вход\n2 - Регистрация\n"
#                        "3 - Завершение работы программы\n")
#         match choice:
#             case "1":
#                 login = input("Введите логин: ")
#                 password = input("Введите пароль: ")
#                 if login in database.data:
#                     if hash(password) == database.data[login].password:
#                         print(f"Вход выполнен, {login}")
#                         break
#                     else:
#                         print("Неверный пароль")
#                         continue
#                     # print("Ok")
#                 else:
#                     print("Пользователь не найден.")
#             case "2":
#                 user = (User(input("Введите логин:"),
#                              input("Введите пароль:"),
#                              input("Введите возраст:")))
#                 # if pwd != pwd2:
#                 #     exit()
#                 user.age
#                 database.add_user(user.username,user)
#             case "3":
#                 break
#             case _:
#                 continue
#         print(database.data)

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
