dias = int(input())

ano = int((dias-dias%365)/365)
dias -= ano*365

mes = int((dias-dias%30)/30)
dias -= mes*30

print("{0} ano(s)\n{1} mes(es)\n{2} dia(s)".format(ano, mes, dias))
