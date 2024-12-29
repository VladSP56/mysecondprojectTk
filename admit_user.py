class User():
    def __init__(self, user_id, name):
        self._user_id = user_id  # Уникальный идентификатор пользователя
        self._name = name  # Имя пользователя
        self._access_level = 'user'  # Уровень доступа для обычных сотрудников

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name  # Исправлено "sefl" на "self"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Уровень доступа для администраторов
        self._users = []  # Список пользователей

    def add_user(self, user):
        self._users.append(user)
        print(f'Пользователь {user.get_name()} добавлен.')

    def remove_user(self, user):
        self._users.remove(user)
        print(f'Пользователь {user.get_name()} удален.')

    def list_users(self):
        print("Список пользователей:")
        for user in self._users:
            print(f'- {user.get_name()} (ID: {user.get_user_id()})')


# Тестирование кода
admin = Admin(user_id=1, name='Alex')
user1 = User(user_id=2, name='Anna')
user2 = User(user_id=3, name='Serge')

# Администратор добавляет пользователей
admin.add_user(user1)  # Админ добавляет пользователя 1
admin.add_user(user2)  # Админ добавляет пользователя 2

# Список пользователей
admin.list_users()

# Удаляем пользователя
admin.remove_user(user2)  # Админ удаляет пользователя 2

# Список пользователей после удаления
admin.list_users()
