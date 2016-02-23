#!/usr/bin/env python
# coding=utf8
from mocks.handler.hello_world import HelloWorldHandler
from pfrock2.core.pfrock_core import PFrock
from pfrock2.plugins.static import add_static_handler

if __name__ == "__main__":
    p_frock = PFrock()

    app = p_frock.make_app()

    # dynamic
    p_frock.add_handler([(r"/", HelloWorldHandler)])

    # static
    add_static_handler(p_frock, 'dir', '/api2/(.*)', "mocks/static")
    add_static_handler(p_frock, 'file', '/api3/my_json', "mocks/static/a.json")

    p_frock.start_app(app)
