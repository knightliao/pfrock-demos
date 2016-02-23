#!/usr/bin/env python
# coding=utf8
import tornado.web


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world2")
