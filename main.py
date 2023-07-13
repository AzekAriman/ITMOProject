import datetime
from jinja2 import Template
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Получение текущего времени
    print_hi('Pycharm')
    print(timestamp)