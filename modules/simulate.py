from utils.clear_terminal import clear_terminal
from utils.pause import pause

def simulate(devices_list):
  clear_terminal()
  print('----- Simulação de consumo -----\n')

  if len(devices_list) == 0:
    print('Sem aparelhos cadastrados!')
    input('\nAperte qualquer tecla para voltar. ')
    clear_terminal()
    return

  try:
    while True:
      try:
        price_per_kwh = float(input('Informe o preço atual do kWh (em R$): '))

        if price_per_kwh <= 0:
          print('O preço deve ser maior que zero. Tente novamente.')
          continue

        break
      except ValueError:
        print('Entrada inválida. Digite um número válido.')

    total_consumption = 0
    total_cost = 0

    print('\nConsumo por aparelho:')
    for device in devices_list:
      monthly_consumption = device['consumo'] * device['horas'] * 30
      monthly_cost = monthly_consumption * price_per_kwh
      total_consumption += monthly_consumption
      total_cost += monthly_cost

      print(f'{device['nome']}: {monthly_consumption:.2f} kWh/mês - R$ {monthly_cost:.2f}/mês')

    print(f'\nConsumo total estimado: {total_consumption:.2f} kWh/mês')
    print(f'Custo total estimado: R$ {total_cost:.2f}/mês')

    input('\nAperte qualquer tecla para voltar. ')
    clear_terminal()
  except Exception as e:
    print('Erro na simulação:', e)
    pause(5)