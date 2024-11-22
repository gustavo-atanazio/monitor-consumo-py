import os
from utils.clear_terminal import clear_terminal
from utils.pause import pause

def generate_report(devices_list):
  clear_terminal()
  print('----- Gerando relatório -----\n')

  reports_dir = 'reports'

  if not os.path.exists(reports_dir):
    os.makedirs(reports_dir)

  report_index = len([file for file in os.listdir(reports_dir) if file.startswith('relatorio_consumo')])
  report_file = os.path.join(reports_dir, f'relatorio_consumo-{report_index + 1}.txt')

  try:
    with open(report_file, 'w') as file:
      file.write('Relatório de Consumo de Energia\n')
      file.write('-' * 30 + '\n')
      total = 0

      # Seção principal do relatório
      for device in devices_list:
        monthly_consumption = device['consumo'] * device['horas'] * 30
        total += monthly_consumption
        file.write(f'{device["nome"]}: {monthly_consumption:.2f} kWh/mês\n')

      file.write(f'\nConsumo total estimado: {total:.2f} kWh/mês\n\n')

      # Seção de dev
      file.write('--- DEV INFO ---\n')

      for index, device in enumerate(devices_list):
        file.write(f'index: {index}\n')
        file.write(f'nome: {device["nome"]}\n')
        file.write(f'consumo: {device["consumo"]}\n')
        file.write(f'horas: {device["horas"]}\n')
        file.write('\n')

      print(f'Relatório gerado com sucesso! Confira o arquivo {report_index + 1} na pasta "reports".')
      pause(3)
  except IOError as e:
    print(f'Erro ao salvar o relatório: {e}')
    pause(3)

def load_report(devices_list):
  clear_terminal()
  print('----- Carregar Relatório -----\n')

  reports_dir = 'reports'

  if not os.path.exists(reports_dir):
    print('Nenhum relatório encontrado. A pasta "reports" está vazia.')
    pause(3)
    return

  reports = [file for file in os.listdir(reports_dir) if file.endswith('.txt')]

  if not reports:
    print('Nenhum relatório encontrado. A pasta "reports" está vazia.')
    pause(3)
    return

  print('Relatórios disponíveis:')
  for i, report in enumerate(reports, start=1):
    print(f'{i}. {report}')

  try:
    choice = int(input('\nEscolha o número do relatório para carregar: '))

    if choice < 1 or choice > len(reports):
      print('Escolha inválida.')
      pause(3)
      return

    report_file = os.path.join(reports_dir, reports[choice - 1])

    with open(report_file, 'r') as file:
      lines = file.readlines()
      dev_info_section = False

      for line in lines:
        if line.strip() == '--- DEV INFO ---':
          dev_info_section = True
          continue

        if dev_info_section:
          if line.startswith('nome:'):
            name = line.split(':', 1)[1].strip()
          elif line.startswith('consumo:'):
            consumption = float(line.split(':', 1)[1].strip())
          elif line.startswith('horas:'):
            hours = float(line.split(':', 1)[1].strip())
            devices_list.append({'nome': name, 'consumo': consumption, 'horas': hours})

      print(f'Relatório "{reports[choice - 1]}" carregado com sucesso!')
      pause(3)
  except (ValueError, IndexError):
    print('Escolha inválida ou erro ao processar o relatório.')
    pause(3)
  except Exception as e:
    print(f'Erro ao carregar o relatório: {e}')
    pause(3)