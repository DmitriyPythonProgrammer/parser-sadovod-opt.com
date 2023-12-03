import core
import parser


def main():
    print('Добро пожаловать в программу для парсинга сайта "https://sadovod-opt.com"')
    print('Проверка подключения')
    if not(core.is_connected()):
        return 0
    print('Создание юзер-агента...')
    agent = core.create_user_agent()
    print('Успешно')
    print('Вставьте ссылку с нужной вам категорией в магазине. (пример: https://sadovod-opt.com/shop/all)')
    general_url = input()
    print('Активация парсинга...')
    parser.main(general_url, agent)
    print('Успешно!\nВ директории, откуда был открыт скрипт, была создана excel таблица с данными.')


if __name__ == "__main__":
    main()


