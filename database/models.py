# Импорт модуля конфигурации с именем 'config'
import config

# Импорт необходимых модулей из SQLAlchemy для работы с базой данных
from sqlalchemy import BigInteger, ForeignKey, String,  Column, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

# Создание асинхронного SQLite-движка с использованием предоставленной конфигурации
engine = create_async_engine(config.SQLITEALHEMY_URL, echo=True)
# Создание асинхронного сессионного объекта для работы с движком
async_session = async_sessionmaker(engine)
# Определение базового класса для декларативного определения моделей данных
class Base(AsyncAttrs, DeclarativeBase):
    pass

# Определение модели данных для пользователя
class User(Base):
    __tablename__ = "user_account"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name = mapped_column(String(30))
    balance: Mapped[int] = mapped_column(default=0)
    registration: Mapped[int] = mapped_column(default=0)
    ban: Mapped[int] = mapped_column(default=0)
    registration_time =  mapped_column(String)
    fuck_time: Mapped[str] = mapped_column(default=0)
    revival_time: Mapped[str] = mapped_column(default=0)
    mode: Mapped[int] = mapped_column(default=0)

    
async def asyn_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
