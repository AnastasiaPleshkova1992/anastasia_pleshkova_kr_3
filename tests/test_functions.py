import pytest

from utils.functions import format_date, mask_card_number, mask_amount_number, get_last_five_operations


def test_format_date():
    assert format_date("2018-09-12T21:27:25.241689") == "12.09.2018"


def test_mask_card_number():
    assert mask_card_number("Visa Platinum 1246377376343588") == "Visa Platinum 1246 73** **** 3588"


def test_mask_amount_number():
    assert mask_amount_number("Счет 14211924144426031657") == "Счет **1657"


def test_get_last_five_operations():
    assert get_last_five_operations() == get_last_five_operations()
