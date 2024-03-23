#3.1
Amigos = ['Ricardo', 'Bassul', 'Joao']
Numero = input("Qual Amigo vc é? (1 a 3)\n")
Numero = int(Numero) - 1
Mensagem = f"paraben1s vc é o {Amigos[Numero]}"
print(Mensagem.title())

#3.3
Carros = ['Honda', 'Lancha', 'A Pé', 'Moto']
Escolha = int(input('Qual meio de andar vc Gosta mais de andar\n')) - 1
print(f"Eu gosto de andar de {Carros[Escolha]}")