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

