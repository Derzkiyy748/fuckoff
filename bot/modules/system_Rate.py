import random
import asyncio
import config

from database.requests import select_all_users, update_rate
from message import message_rate

async def choose_numbers_by_percentages(percentages):
    """
    Choose two different numbers based on the provided percentages.

    Parameters:
    - percentages (dict): A dictionary where the key is the number, and the value is the percentage chance.

    Returns:
    - int: The first chosen number.
    - int: The second chosen number.
    """
    random_numbers = random.sample(range(100), 2)
    current_percentage = 0

    chosen_numbers = []
    for rand_num in random_numbers:
        current_percentage = 0
        for number, percentage in percentages.items():
            current_percentage += percentage
            if rand_num <= current_percentage:
                chosen_numbers.append(number)
                break

    if len(chosen_numbers) == 2:
        return (chosen_numbers)

    return next(iter(percentages.keys())), next(iter(percentages.keys()))


async def system_rate(bot):
    number_percentages = config.RATE_PERCENTAGES

    while True:
        users = await select_all_users()
    
        for user in users:
            user_id = user.user_id
            chosen_number = await choose_numbers_by_percentages(number_percentages)
           
            await update_rate(float(chosen_number[0]), float(chosen_number[1]))
            await bot.send_message(user_id, message_rate(chosen_number), parse_mode='html')
            await asyncio.sleep(config.TIME)
        await asyncio.sleep(config.TIME)