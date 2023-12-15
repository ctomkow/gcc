
import parser as main

test_data1 = "six1mpffbnbnnlx7three\n"
test_data2 = "sixmpffbnbnnlxthree\n"
test_data3 = "six22222mpffbnbnnlxthree\n"
test_data4 = "sixmpffbnbn9nlxthree\n"


def test_parse_from_left_data1():
    assert main.parse_from_left(test_data1) == '1'


def test_parse_from_left_data2():
    assert main.parse_from_left(test_data2) == ''


def test_parse_from_left_data3():
    assert main.parse_from_left(test_data3) == '2'


def test_parse_from_left_data4():
    assert main.parse_from_left(test_data4) == '9'


test_parse_from_left_data1()
test_parse_from_left_data2()
test_parse_from_left_data3()
test_parse_from_left_data4()
