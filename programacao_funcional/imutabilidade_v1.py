#!/usr/bin/python3
from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses do ano com 31 dias

meses_com_31_index = filter(lambda mes: mdays[mes] == 31, range(1, 13))
meses_com_31 = map(lambda index: month_name[index], meses_com_31_index)
meses_com_31_str = reduce(
        lambda meses, mes: f'{meses}\n- {mes}',
        meses_com_31,
        'Meses com 31 dias: '
)  

print(meses_com_31_str)
