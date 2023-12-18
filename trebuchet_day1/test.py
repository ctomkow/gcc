
import parser

import unittest


class TestParsing(unittest.TestCase):

    test_data1 = "six1mpffbnbnnlx7three\n"
    test_data2 = "sixmpffbnbnnlxthree\n"
    test_data3 = "six22222mpffbnbnnlxthree\n"
    test_data4 = "sixmpffbnbn9nlxthree\n"
    test_data5 = 42

    def test_parse_from_left_data1(self):
        assert parser.parse_from_left(self.test_data1) == '1'

    def test_parse_from_left_data2(self):
        assert parser.parse_from_left(self.test_data2) == ''

    def test_parse_from_left_data3(self):
        assert parser.parse_from_left(self.test_data3) == '2'

    def test_parse_from_left_data4(self):
        assert parser.parse_from_left(self.test_data4) == '9'

    def test_parse_from_left_data5(self):
        self.assertRaises(TypeError, parser.parse_from_left, self.test_data5)


TestParsing().test_parse_from_left_data1()
TestParsing().test_parse_from_left_data2()
TestParsing().test_parse_from_left_data3()
TestParsing().test_parse_from_left_data4()
