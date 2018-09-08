# -*- coding: utf-8 -*-

"""
bot.app
~~~~~~~

"""

import sched
import threading
import time

from flask import Flask, Response, request
from structlog import get_logger
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import (
    ViberConversationStartedRequest,
    ViberFailedRequest,
    ViberMessageRequest,
    ViberSubscribedRequest,
    ViberUnsubscribedRequest,
)

from bot.webhook import set_webhook, setup_viber_api


HOST = "127.0.0.1"
PORT = 8080
DEBUG = True


app = Flask(__name__)
viber = setup_viber_api()
log = get_logger()


@app.route("/", methods=["POST"])
def incoming():
    log.debug("received request", post_data=request.get_data())

    viber_request = viber.parse_request(request.get_data())
    req_types = (
        ViberConversationStartedRequest,
        ViberSubscribedRequest,
        ViberUnsubscribedRequest,
    )

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
    elif isinstance(viber_request, req_types):
        viber.send_messages(
            viber_request.sender.id,
            [TextMessage(None, None, viber_request.get_event_type())],
        )
    elif isinstance(viber_request, ViberFailedRequest):
        log.warn("client failed receiving message", failure=viber_request)

    return Response(status=200)


def main():
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(5, 1, set_webhook, (viber,))
    thr = threading.Thread(target=scheduler.run)
    thr.start()

    app.run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == "__main__":
    main()
