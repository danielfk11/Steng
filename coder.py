from stegano import lsb

perg = input("Qual mensagem deseja passar?\n-> ")

secret = lsb.hide("pass.png", "{}".format(perg))
secret.save(".secret.png")