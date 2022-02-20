from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    return date.strftime('%d/%m/%Y')

def str_para_date(data: str) -> date:
    return datetime.strftime(data, '%d/%m/%Y')

def format_float_str_moeda(valor: float) ->str:
    return f'R$ {valor:,.2f}'