# Monitor de consumo de energia

Este é um programa em Python desenvolvido para gerenciar, simular e gerar relatórios sobre o consumo de energia de equipamentos. É eficaz principalmente para estimar custos de consumo e auxiliar no monitoramento.

## 🛡️ Requisitos

- Python 3.13.0 ou superior.
- Sistema operacional com suporte ao comando `clear` ou `cls` para limpar o terminal.

## 🛠️ Estrutura do projeto

```
.
├── modules
│   ├── register_device.py  # Cadastro de dispositivos
│   ├── report.py           # Geração e carregamento de relatórios
│   ├── simulate.py         # Simulação de consumo
├── reports                 # Pasta onde os relatórios são salvos
├── utils
│   ├── clear_terminal.py   # Limpeza do terminal
│   ├── pause.py            # Pausa temporária
└── main.py                 # Arquivo principal para execução do programa
```

---

## 📋 Funcionalidades

1. **Cadastro de equipamentos**:
   - Permite registrar dispositivos, informando o nome, consumo em kWh e horas de uso diário.

2. **Simulação de consumo**:
   - Simula o consumo mensal de energia de todos os dispositivos cadastrados.
   - Calcula o custo total baseado no preço do kWh informado pelo usuário.

3. **Geração de relatórios**:
   - Gera um arquivo de texto com o consumo de cada dispositivo e consumo total.
   - Os relatórios são armazenados na pasta `reports` e nomeados sequencialmente.

4. **Carregamento de relatórios**:
   - Permite carregar um relatório existente, preenchendo a lista de dispositivos com os dados salvos.

---

## 🚀 Como executar

1. Certifique-se de ter o Python 3.13.0 (ou superior) instalado.
2. Clone este repositório ou baixe os arquivos.
3. Navegue até a pasta raiz do projeto.
4. Execute o programa com:

  ```bash
   python main.py
  ```
---

## 🧩 Detalhes técnicos

### **Módulos principais**
- **`main.py`**:
  - Contém o menu principal com as opções disponíveis.
  - Faz a chamada para os módulos e funções específicas.

- **`register_device.py`**:
  - Realiza o cadastro de novos dispositivos.
  - Exemplo de entrada:
    ```
    Nome do equipamento: Geladeira
    Consumo em kWh: 2.0
    Horas de uso diário: 24
    ```

- **`simulate.py`**:
  - Calcula o consumo mensal e o custo estimado para os dispositivos cadastrados.
  - Exige que o usuário informe o preço do kWh:
    ```
    Informe o preço atual do kWh (em R$): 0.50
    ```

- **`report.py`**:
  - Gera relatórios e permite carregar relatórios existentes.

### **Utilitários**
- **`clear_terminal.py`**:
  - Limpa o terminal para melhorar a visualização.
- **`pause.py`**:
  - Pausa o programa por determinado tempo.

---

## 📂 Exemplo de relatório

Um relatório gerado será salvo na pasta `reports` e terá o seguinte formato:

```
Relatório de Consumo de Energia
------------------------------
Geladeira: 1440.00 kWh/mês
TV: 300.00 kWh/mês

Consumo total estimado: 1740.00 kWh/mês

--- DEV INFO ---
index: 0
nome: Geladeira
consumo: 2.0
horas: 24

index: 1
nome: TV
consumo: 0.5
horas: 20
```

---

## Autor
Gustavo Atanazio <br>
RM: 559098