#!/usr/bin/env python
# coding=utf8
import tornado.web

grower_index = 0


class PersistenceHandler(tornado.web.RequestHandler):
    def get(self):
        global grower_index
        grower_index += 1
        self.write("Hello, world " + str(grower_index))
