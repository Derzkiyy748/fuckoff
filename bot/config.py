#   ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ И БОТА
#-------------------------------------------------------------#
TOKEN = '6341138136:AAE-8UbHtD1xAn-kzVXjXZjpApEfcqtaOfM'
SQLITEALHEMY_URL = "sqlite+aiosqlite:///fuckoff/bot/database/db.sqlite3"
link = 'https://telegra.ph/KAK-POLUCHIT-ZHIZNI-I-UDARY-V-BOTE-02-24'
#-------------------------------------------------------------#
#-------------------------------------------------------------#

TIME = 60 * 60

RATE_PERCENTAGES = {1.5: 60, 2: 40, 3: 35, 4: 30, 5: 20, 10: 5}

ADMIN_ID = {1059702390}

#   НАСТРОЙКИ БОНУСА У КАЖДОГО РАНГА
#-------------------------------------------------------------#
fresh_bonus_fuck = 10
fresh_bonus_lifes = 10

lox_bonus_fuck = 30
lox_bonus_lifes = 30

nikto_bonus_fuck = 40
nikto_bonus_lifes = 40

norm_chel_bonus_fuck = 50
norm_chel_bonus_lifes = 50

krutoy_chel_bonus_fuck = 60
krutoy_chel_bonus_lifes = 60

pacan_bonus_fuck = 70
pacan_bonus_lifes = 70

zabivnoy_bonus_fuck = 80
zabivnoy_bonus_lifes = 80

glavniy_bonus_fuck = 90
glavniy_bonus_lifes = 90
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   СЛОВАРЬ ДЛЯ РАБОТЫ ОБНОВЛЕНИЯ БОНУСА
#-------------------------------------------------------------#
bonuses = {
            'fresh': (fresh_bonus_fuck, fresh_bonus_lifes),
            'лох': (lox_bonus_fuck, lox_bonus_lifes),
            'никто': (nikto_bonus_fuck, nikto_bonus_lifes),
            'норм чел': (norm_chel_bonus_fuck, norm_chel_bonus_lifes),
            'крутой чел': (krutoy_chel_bonus_fuck, krutoy_chel_bonus_lifes),
            'пацан': (pacan_bonus_fuck, pacan_bonus_lifes),
            'забивной': (zabivnoy_bonus_fuck, zabivnoy_bonus_lifes),
            'главный': (glavniy_bonus_fuck, glavniy_bonus_lifes),
        }

photo_rank = {
    'лох': 'photo_rank/лох.jpg',
    'никто': 'photo_rank/никто.jpg',
    'норм чел': 'photo_rank/норм_чел.jpg',
    'крутой чел': 'photo_rank/крутой_чел.jpg',
    'пацан': 'photo_rank/пацан.jpg',
    'забивной': 'photo_rank/забивной.jpg',
    'главный': 'photo_rank/главный.jpg',
    'fresh': 'photo_rank/fresh.jpg'
}
print('Фото ранга воркает!')
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   ОПРЕДЕЛЯЕТ РАНГ НА ОСНОВЕ ЗНАЧЕНИЯ УДАРОВ
#-------------------------------------------------------------#
def determine_rank(fuck_value: int) -> str:
    # Определение ранга на основе значения fuck
    if fuck_value == 1000:
        return 'главный'
    elif fuck_value == 800:
        return 'забивной'
    elif fuck_value == 600:
        return 'пацан'
    elif fuck_value == 450:
        return 'крутой чел'
    elif fuck_value == 250:
        return 'норм чел'
    elif fuck_value == 150:
        return 'никто'
    elif fuck_value == 1:
        return 'лох'
    else:
        return 'fresh'
#-------------------------------------------------------------#


#   СИСТЕМА СЧЕТА ДО СЛЕДУЮЩЕГО РАНГА
#-------------------------------------------------------------#
def next_rank(user_fuck: int, user_rank: str):
    if user_rank == 'главный':
        return 'Вы достигли п'
    elif user_rank == 'забивной':
        return 1000 - user_fuck
    elif user_rank == 'пацан':
        i = 800 - user_fuck
        return i
    elif user_rank == 'крутой чел':
        i = 600 - user_fuck
        return i
    elif user_rank == 'норм чел':
        i = 450 - user_fuck
        return i
    elif user_rank == 'никто':
        i = 250 - user_fuck
        return i
    elif user_rank == 'лох':
        i = 150 - user_fuck
        return i
    else:
        return 1 - user_fuck
#-------------------------------------------------------------#
