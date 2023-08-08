import unittest

from src.tools.crc16 import Tools


class ToolsTest(unittest.TestCase):
    def test_should_crc16(self):
        self.assertEqual("5749", Tools.crc16("abc"))

    def test_should_crc16_with_empty_string(self):
        self.assertEqual("FFFF", Tools.crc16(""))
