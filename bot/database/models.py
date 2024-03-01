#   Импорт модуля конфигурации с именем 'config'
#-------------------------------------------------------------#
import config
import DateTime
import datetime
from datetime import datetime
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   Импорт необходимых модулей из SQLAlchemy для работы с базой данных
#-------------------------------------------------------------#
from sqlalchemy import String, Column, CHAR
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   Создание асинхронного SQLite-движка с использованием предоставленной конфигурации
#-------------------------------------------------------------#
engine = create_async_engine(config.SQLITEALHEMY_URL, echo=True)
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   Создание асинхронного сессионного объекта для работы с движком
#-------------------------------------------------------------#
async_session = async_sessionmaker(engine)
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   Определение базового класса для декларативного определения моделей данных
#-------------------------------------------------------------#
class Base(AsyncAttrs, DeclarativeBase):
    pass
#-------------------------------------------------------------#
#-------------------------------------------------------------#


#   Определение модели данных для пользователя
#-------------------------------------------------------------#
class User(Base):
    __tablename__ = "user_account"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[int] = mapped_column(default=0)
    nick: Mapped[str] = mapped_column()
    rank: Mapped[str] = mapped_column(default='fresh')
    vip_rank: Mapped[str] = mapped_column(default='бомж')
    registration: Mapped[int] = mapped_column(default=0)
    ban: Mapped[int] = mapped_column(default=0)
    lives: Mapped[int] = mapped_column(default=10)
    fuck: Mapped[int] = mapped_column(default=10)
    registration_time =  mapped_column(String)
    fucked_up: Mapped[int] = mapped_column(default=0)
    bonus_time: Mapped[int] = mapped_column(default=datetime.utcnow)
    mode: Mapped[int] = mapped_column(default=0)
#-------------------------------------------------------------#
#-------------------------------------------------------------#

    
#   ФУНКЦИЯ СОЗДАНИЯ ТАБЛИЦ
#-------------------------------------------------------------#
async def asyn_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
#-------------------------------------------------------------#
#-------------------------------------------------------------#




