import json
import os

from config import ROOT_DIR

OPERATION_PATH = os.path.join(ROOT_DIR, 'operations.json')


def format_date(date):
    """Получает отформатированную дату
    """
    formatted_date = date.split('T')[0].split('-')
    formatted_date = '{}.{}.{}'.format(formatted_date[2], formatted_date[1], formatted_date[0])
    return formatted_date


def mask_card_number(card_number):
    """Получает замаскированный номер карты
    """
    masked_number = '{} {}** **** {}'.format(card_number[:-12], card_number[-10:-8], card_number[-4:])
    return masked_number


def mask_amount_number(amount_number):
    """Получает замаскированный вид счета
    """
    masked_amount = 'Счет **{}'.format(amount_number[-4:])
    return masked_amount

