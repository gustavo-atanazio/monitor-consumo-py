from utils.clear_terminal import clear_terminal
from utils.pause import pause

def register_device(devices_list):
  clear_terminal()
  print('----- Registrar aparelho -----\n')

  try:
    name = input('Nome do equipamento: ')
    consumption = float(input('Consumo em kWh: '))
    hours = float(input('Horas de uso diário: '))

    devices_list.append({
      'nome': name,
      'consumo': consumption,
      'horas': hours
    })

    print(f'\n{name} cadastrado com sucesso!')
    pause(2)
  except ValueError:
    print('Entrada inválida! Certifique-se de inserir números para consumo e horas.')
    pause(2)