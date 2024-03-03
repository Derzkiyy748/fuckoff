from aiogram import BaseMiddleware, Bot
from modules.Filters import Filter
from aiogram.types import Message
from database.requests import select_user
import asyncio
from aiogram import types, Dispatcher





# Define your ExchangeRateMiddleware
class ExchangeRateMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        # Check if the message is a private message and not a reply
        if message.chat.type == "private" and not message.reply_to_message:
            # Send a message about the updated exchange rate
            await message.answer("🔄 Обновленный курс обмена:\n1 коин на жизни и удары.")

    async def send_periodic_messages(self, bot: Bot, dp: Dispatcher):
        while True:
            # Fetch the list of users to send messages
            users = await select_user()

            # Extract user IDs from the list
            user_ids = [user.id for user in users]

            # Send messages to each user
            for user_id in user_ids:
                try:
                    await bot.send_message(user_id, "🔄 Обновленный курс обмена:\n1 коин на жизни и удары.")
                except Exception as e:
                    # Handle errors or exceptions while sending messages
                    print(f"Error sending message to user {user_id}: {e}")

            # Wait for 24 hours before sending messages again
            await asyncio.sleep(5)

    async def __call__(self, *args, **kwargs):
        pass