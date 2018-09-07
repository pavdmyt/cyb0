# -*- coding: utf-8 -*-

"""
bot.webhook
~~~~~~~~~~~

"""

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

from bot.config import BOT_AUTH_TOKEN, BOT_NAME, BOT_PIC_URL, PUBLIC_URL


def setup_viber_api():
    api = Api(
        BotConfiguration(
            name=BOT_NAME, avatar=BOT_PIC_URL, auth_token=BOT_AUTH_TOKEN
        )
    )
    return api


def set_webhook(viber_api):
    viber_api.set_webhook(PUBLIC_URL)
