#!/usr/bin/env python
# coding=utf8

from pfrock.core.web import PfrockRequestDispatcher

grower_index = 0


class PersistenceHandler(PfrockRequestDispatcher):
    def get(self):
        global grower_index
        grower_index += 1
        self.write("Hello, world " + str(grower_index))
