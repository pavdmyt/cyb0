# -*- coding: utf-8 -*-

"""
bot.config
~~~~~~~~~~

Configuration data.
"""

import configparser
import os


_this_dir = os.path.dirname(os.path.realpath(__file__))
_fpath = os.path.join(os.path.dirname(_this_dir), ".secrets")
_cfg = configparser.ConfigParser()
_cfg.read(_fpath)


BOT_NAME = _cfg["viber-bot"]["name"]
BOT_PIC_URL = _cfg["viber-bot"]["avatar"]
PUBLIC_URL = _cfg["viber-bot"]["publicUrl"]
BOT_AUTH_TOKEN = _cfg["viber-bot"]["authToken"]
