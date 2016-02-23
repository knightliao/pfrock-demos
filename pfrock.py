#!/usr/bin/env python
# coding=utf8
import logging
from logging.config import dictConfig

import tornado.options

from pfrock2.core import PFrock
from pfrock2.plugins.handler import add_handler
from pfrock2.plugins.proxy import add_proxy_handler
from pfrock2.plugins.static import add_static_handler

if __name__ == "__main__":
    p_frock = PFrock()

    app = p_frock.make_app()

    logging_config = dict(
        version=1,
        loggers={
            'pfrock.proxy': {'level': logging.DEBUG},
            'tornado': {'level': logging.DEBUG},
            'pfrock.static': {'level': logging.DEBUG}
        }
    )
    dictConfig(logging_config)
    tornado.options.parse_command_line()

    # dynamic
    add_handler(p_frock, r"/api", 'mocks.handler.hello_world.HelloWorldHandler')

    # static
    add_static_handler(p_frock, 'dir', '/api2/(.*)', "mocks/static")
    add_static_handler(p_frock, 'file', '/api3/my_json', "mocks/static/a.json")
    add_static_handler(p_frock, 'file', '/api3/my_json2', "mocks/static/b.json")
    add_proxy_handler(p_frock, '.*', "http://tieba.baidu.com/", "tieba.baidu.com")

    p_frock.start_app(app)
