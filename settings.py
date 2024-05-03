from dataclasses import dataclass

from environs import Env


@dataclass
class Bot:
    bot_token: str
    admin_id: int


@dataclass
class Settings:
    bot: Bot


def get_settings(path: str):
    env = Env()

    env.read_env(path)

    return Settings(
        bot=Bot(
            bot_token=env.str("BOT_TOKEN"),
            admin_id=env.int("ADMIN_ID")
        ),
    )


settings = get_settings('.input')
