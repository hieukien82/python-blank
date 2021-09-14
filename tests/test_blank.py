# -*- coding: utf-8 -*-
import blank


def test_blank_package():
    my_str = "hieukien"
    rev_str = blank.reverse(my_str)
    assert rev_str == "neikueih"
