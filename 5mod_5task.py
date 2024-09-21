# Дополнительное практическое задание по модулю 5
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname            # nickname (имя пользователя, строка)
        self.password = hash(password)      # password (в хэшированном виде, число)
        self.age = age                      # age (возраст, число)

    def __str__(self):  # сделел для работы поиска
        return f'{self.nickname}'


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title                  # title (заголовок, строка)
        self.duration = duration            # duration (продолжительность, секунды)
        self.time_now = time_now            # time_now (секунда остановки (изначально 0))
        self.adult_mode = adult_mode        # adult_mode (ограничение по возрасту, bool (False по умолчанию)

    def __str__(self):  # сделел для работы поиска
        return f'{self.title}'


class UrTube:
    def __init__(self):
        self.users = []           # users(список объектов User)
        self.videos = []          # videos(список объектов Video)
        self.current_user = None    # current_user(текущий пользователь, User)

    def add(self, *args):  # метод позволяющий добовлять в список videos экземпляра класса UrTube отсутствующие там экземпляры класса Video
        for i in args:
            if i in self.videos or not isinstance(i, Video):
                # print('Видео уже имеется в списке класса UrTube, или такого экземпляра в классе Video нет')   # для проверки
                continue
            else:
                self.videos.append(i)

    def get_videos(self, search):
        search_list = []
        for i in self.videos:
            if search.upper() in str(i).upper():
                search_list.append(str(i))
            else:
                continue
        return search_list

    def register(self, nickname, password, age):
        flag = 0
        for i in self.users:
            if nickname == str(i):
                flag += 1
        if flag == 0:
            new_video = User(nickname, password, age)
            self.users.append(new_video)
            self.current_user = new_video
            # print(f'Вы зарегистрированы, добро пожаловать, {nickname}, вход выполнен.') #, для проверки, тут автоматически вход в акаунт после регистрации
        else:
            print(f'Пользователь {nickname} уже существует')
        # print(self.users) # для проверки

    def log_in(self, nickname, password): # в тесте не учавствует...???
        flag = 0
        for i in self.users:
            if nickname == i.nickname:
                flag += 1
                if hash(password) == i.password:
                    self.current_user = i
                    print(f'Добро пожаловать, {i.nickname}')
                else:
                    print('Вы ввели неверный пароль')
                break
            else:
                continue
        if flag == 0:
            print(f'Позьзователь {nickname} не зарегистрирован.')


    def watch_video(self, title_video):
        if self.current_user is not None:
            for i in self.videos:
                if title_video in str(i):
                    age = self.current_user.age # нужно достать из users???
                    duration = i.duration # нужно достать из videos???
                    age_stop = i.adult_mode
                    if (age >= 18 and age_stop == True) or age_stop == False:
                        for j in range(1, duration + 1):
                            sleep(1)
                            print(j)
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу (возрастное ограничение)')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')



# if __name__ == '__main__':
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


# Добавление видео
ur.add(v1, v2)
# ur.add(v2, v1, v2, 3, 'super') # проверка
# print(ur.videos) # проверка

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# # ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25) # для проверки
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Проверка авторизации (нет в задании)
print('----------------------------------------')
print('Проверки приведенной ниже нет в задании:')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.log_in('kolya', 'lolkekcheburek')
ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')










