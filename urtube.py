from time import sleep

from users import User
from database import Database
from dbvideo import DBVideo


class UrTube:
    def __init__(self):
        # self.database =
        self.users = Database()
        self.videos = DBVideo()
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users.data:
            if hash(password) == self.users.data[nickname].password:
                print(f"Вход выполнен, {nickname}")
                self.current_user = nickname
            else:
                print("Неверный пароль")

    def register(self, nickname, password, age):
        if nickname not in self.users.data:
            user = User(nickname, password, age)
            self.users.add_user(nickname, user)
            self.current_user = nickname
        else:
            print(f"Пользователь {nickname} уже существует.")

    def logout(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video.title not in self.videos.data:
                self.videos.add_video(video.title, video)

    def get_videos(self, name):
        # l = name.lower()
        found = list()
        for k in self.videos.data:
            if name.lower() in k.lower():
                found.append(k)
        if len(found) == 0:
            found = "Nothing found"
        return found

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if title in self.videos.data:
            if self.videos[title].adult_mode and self.users[self.current_user].age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            for k in range(self.videos[title].duration):
                sleep(1)
                self.videos[title].time_now = k
                print(f"{k}\n")
            print("Конец видео")
            return
