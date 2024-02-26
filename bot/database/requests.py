import datetime
from datetime import datetime
from datetime import timedelta

from database.models import User, async_session
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from config import bonuses, determine_rank, next_rank
from typing import Tuple, Union



async def registration_user(user_id: int, data: dict) -> User:
    async with async_session() as session:
        existing_user = await session.get(User, user_id)
        if existing_user:

            return False

        new_user = User(user_id=user_id, **data)
        session.add(new_user)
        await session.commit()

        return new_user
    

async def get_user(user_id: int) -> User:
    async with async_session() as session:
        user = await session.get(User, user_id)

        return user
    

async def update_fuck(user_id: int, number: int):
    async with async_session() as session:
        res = await session.execute(select(User.fuck, User.fucked_up).where(User.user_id == user_id))
        row = res.fetchone()

        if row is not None:
            current_fuck, current_fucked_up = row
            if current_fuck >= number:
                await session.execute(
                    update(User)
                    .where(User.user_id == user_id)
                    .values(fuck=current_fuck - number, fucked_up=current_fucked_up + 1)
                )
                await session.commit()
        return


async def update_lives(opponent_id: int, number: int):
    async with async_session() as session:
        res = await session.execute(select(User.lives).where(User.user_id == opponent_id))
        livess = res.scalar()

        if livess > 0:
            await session.execute(update(User).where(User.user_id == opponent_id).values(lives = livess - number))
            await session.commit()


async def select_user(user_id: int):
    async with async_session() as session:
        # Используем selectinload('*') для выбора всех столбцов из модели User
        res = await session.execute(select(User).where(User.user_id == user_id).options(selectinload('*')))
        user = res.scalar()

        return user
    

async def select_opponent(opponent_id: int):
    async with async_session() as session:
        res = await session.execute(select(User).where(User.user_id == opponent_id).options(selectinload('*')))
        user = res.scalar()

        return user
    

async def update_bonus_user(user_id: int, rank: str):
    async with async_session() as session:
        # Получаем время последнего забора бонуса
        res = await session.execute(select(User.bonus_time).where(User.user_id == user_id))
        bonus_time_str = res.scalar()

        # Убедитесь, что bonus_time является объектом datetime
        bonus_time = datetime.strptime(bonus_time_str, "%Y-%m-%d %H:%M:%S.%f")

        # Проверяем, прошло ли 5 минут с момента последнего забора бонуса
        time_since_last_bonus_claim = datetime.utcnow() - bonus_time
        if time_since_last_bonus_claim < timedelta(minutes=1):
            return False

        # Если прошло 5 минут, обновляем бонусы и время последнего забора
        if rank in bonuses:
            bonus_fuck, bonus_lifes = bonuses[rank]

            await session.execute(
                update(User)
                .where(User.user_id == user_id)
                .values(
                    fuck=User.fuck + bonus_fuck, lives=User.lives + bonus_lifes,
                    bonus_time=datetime.utcnow() 
                )
            )
            await session.commit()

            return True, bonus_fuck, bonus_lifes
        else:
            return False


            


# В функции update_rank_user
async def update_rank_user(user_id: int) -> Tuple[bool, Union[int, str, int]]:
    async with async_session() as session:
        # Получаем текущее значение fuck и текущий ранг пользователя
        res = await session.execute(select(User.fucked_up, User.rank).where(User.user_id == user_id))
        fuck_value, current_rank = res.first()

        # Определяем новый ранг на основе значения fuck
        new_rank = determine_rank(fuck_value)

        if new_rank != current_rank:    # Проверяем, нужно ли обновлять ранг
            await session.execute(     
                update(User)
                .where(User.user_id == user_id)  # Обновляем ранг пользователя в базе данных
                .values(rank=new_rank)
            )
            await session.commit()
            res = await session.execute(select(User.fucked_up, User.rank).where(User.user_id == user_id))
            user_score, rank = res.first()
            new_score_user = next_rank(user_score, rank)
            return True, new_rank, new_score_user  # Возвращаем True, новый ранг и количество fuck до нового ранга, если ранг изменился
        else:
            res = await session.execute(select(User.fucked_up, User.rank).where(User.user_id == user_id))
            user_score, rank = res.first()

            new_score_user = next_rank(user_score, rank)
            return False, current_rank, new_score_user  # Возвращаем False, текущий ранг и количество текущих fuck, если ранг не изменился


async def score_rang(user_id: int) -> int:
    async with async_session() as session:
        res = await session.execute(select(User.fucked_up, User.rank).where(User.user_id == user_id))
        score_ran, rang = res.first()

        user_score = next_rank(score_ran, rang)
        return user_score



           