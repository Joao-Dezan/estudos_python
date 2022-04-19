#!/usr/bin/python3
from calendar import mdays, month_name
from functools import reduce
from locale import setlocale, LC_ALL

# Português do Brasil
setlocale(LC_ALL, 'pt_BR.UTF-8')


def mes_com_31(mes): return mdays[mes] == 31


def get_nome_mes(mes): return month_name[mes]


def juntar_meses(todos, nome_mes): return f'{todos}\n- {nome_mes}'


meses_com_31_index = filter(mes_com_31, range(1, 13))
meses_com_31 = map(get_nome_mes, meses_com_31_index)
meses_com_31_str = reduce(juntar_meses, meses_com_31, 'Meses com 31 dias: ')

print(meses_com_31_str)

