import textwrap

def no_start_text():
    return textwrap.dedent('''
    Добро пожаловать в бота уебан!

    Здесь ты можешь уебать любого человека и объявить его уебаном!
    Небойся, за это тебе ничего не будет, лишь только можешь получить в ответ)

    Для ознакомления с командами, введите /help
    Кнопочки снизу)
    ''')

def yes_start_text():
    return textwrap.dedent('''
    Как я вижу по своим уебским базам, вы уже зарегистрированы, увы..

    Для ознакомления с командами, введите /help
    все полезные кнопочки снизу
    ''')

def commands_text():
    return textwrap.dedent('''
    Команды:
    /start - Начало работы с ботом
    /help - Помощь
    уебать (ответ на сообщение) - Уебать любого человека
    ''')

def help_text():
    return textwrap.dedent('''
    dddd
    ''')


def reply_message(opponent_name, opponent_username, selected_user, opponent, next_rang):
    return textwrap.dedent(f'''
        ┎Ты успешно уебал уебка! <a href='https://t.me/@{opponent_username}/'>{opponent_name}</a>👊
        ┃
        ┣У тебя остался(ось) {selected_user.fuck} удар(ов)🔰
        ┖У <a href='https://t.me/@{opponent_username}/'>{opponent_name}</a>, осталось {opponent.lives} жизнь(ей)❤️
        ┖До нового ранга: {next_rang}
    ''')


trigger = ['уебать', 'Уебать', 'Ебнуть', 'ебануть', 'Ебануть', 'ебнуть', 'fuck']