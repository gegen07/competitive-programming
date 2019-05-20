salario = float(input())

if salario >= 0.0 and salario <= 2000.0:
  print("Isento")
elif salario >= 2000.01 and salario <= 3000.0:
  imposto = ((salario - 2000) * 0.08)
  print("R$ {:.2f}".format(imposto))
elif salario >= 3000.01 and salario <= 4500.0:
  imposto = ((salario -(salario-3000) - 2000) * 0.08) + ((salario-3000) * 0.18)
  print("R$ {:.2f}".format(imposto))
elif salario > 4500.0:
  imposto = ((salario -(salario-3000) - 2000) * 0.08) + ((salario -(salario-4500) -3000) * 0.18) + ((salario - 4500) * 0.28)
  print("R$ {:.2f}".format(imposto))
