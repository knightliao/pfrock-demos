#!/usr/bin/env python
# coding=utf8
from pfrock.core.web import PfrockRequestDispatcher


class HelloWorldHandler(PfrockRequestDispatcher):
    def get(self):
        self.write("Hello, world")
