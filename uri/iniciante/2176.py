mensagem = input()
qtd1Mensagem = 0

qtd1Mensagem = mensagem.count("1")
if qtd1Mensagem % 2 != 0:
    print("{}1".format(mensagem))
else:
    print("{}0".format(mensagem))
