menu = """
  Bem-vindo ao seu banco virtual!!!

  Por favor, selecione uma opção.

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "d":
    valor = float(input("Informe o valor do depósito "))

    if valor > 0:
      saldo += valor
      extrato += f"Depósito de R$ {valor:.2f}\n"

    else:
      print("Não foi possível realizar o depósito")
      

  elif opcao == "s":
    valor = float(input("Informe o valor do saque "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Não foi possível sacar, o valor excedeu o seu saldo!")

    elif excedeu_limite:
      print("Não foi possível sacar, o valor excedeu seu limite!")

    elif excedeu_saques:
      print("Você excedeu seu número de saques!")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque de R$ {valor:.2f}\n"
      numero_saques += 1

    else:
      print("O valor informado é inválido!")

  elif opcao == "e":
    print("\n==================Extrato==================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==================================================")



  elif opcao == "q":
    print("Sair")
    break
  
  else:
    print("Opção inválida")
