# 1 Lambda-функция:
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
res = map(lambda x, y: x == y, first, second)

print(list(res))


# 2 Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            write_everything = [file.write(str(x) + '\n') for x in data_set]

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3 Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
