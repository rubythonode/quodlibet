# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

from tests import TestCase

from quodlibet.update import UpdateDialog


class TUpdateDialog(TestCase):

    def test_main(self):
        UpdateDialog(None).destroy()