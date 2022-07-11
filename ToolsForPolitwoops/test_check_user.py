# -*- coding: utf-8 -*-

from check_user import check_username

def test_check_username():
    existing_user = "SenRickScott"
    assert(check_username(existing_user))