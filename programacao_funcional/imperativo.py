#!/usr/bin/python3
from locale import LC_ALL, setlocale
from calendar import mdays, month_name

# Português do Brasil
setlocale(LC_ALL, 'pt_BR.UTF-8')

# Listar todos os meses com 31 dias

print('Meses com 31 dias: ')
for mes in range(1, 13):
    if mdays[mes] == 31:
        print(f'- {month_name[mes]}')
