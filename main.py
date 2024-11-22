from modules.register_device import register_device
from modules.simulate import simulate
from modules.report import generate_report
from modules.report import load_report
from utils.pause import pause

def main():
  options = [
    { 'name': 'Cadastrar equipamento', 'callback': register_device },
    { 'name': 'Simular consumo', 'callback': simulate },
    { 'name': 'Gerar relatório', 'callback': generate_report },
    { 'name': 'Carregar relatório', 'callback': load_report },
    { 'name': 'Sair' }
  ]
  devices = []

  while True:
    print('\n----- Monitor de consumo -----')

    for i, opt in enumerate(options):
      print(f'{i + 1}. {opt['name']}')

    option = input('Escolha uma opção: ')

    if not option.isnumeric():
      print('Digite apenas números.')
      pause(1)
      continue

    option = int(option)

    if options[option - 1]['name'] == 'Sair':
      print('Encerrando o programa...')
      break

    options[option - 1]['callback'](devices)

main()