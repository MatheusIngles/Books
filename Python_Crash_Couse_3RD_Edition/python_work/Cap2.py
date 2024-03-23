#2.3
Nome = input("Escreva seu nome?\n")
print(f"Ola! {Nome}, gostaria de aprender um pouco de python hoje??")

#2.4
Name_peable = input("Seu nome?\n")
print(f"{Name_peable.upper()}, {Name_peable.lower()}, {Name_peable.title()}")

#2.5 e 2.6
Autor = "Forrest Gump";
Frase = f"{Autor}, disse uma vez que 'A vida é como uma caixa de chocolates, você nunca sabe o que vai encontrar...'"
print(Frase.title())

#2.7
Nome = input("Gosante?\n")
Nome = f" {Nome} "
print(f"\n\t Nome \n")
print(Nome.strip())
print(Nome.lstrip())
print(Nome.rstrip())

# 2.8
Pi = 'Fazer amigos é genial'
Coisa_ruim = Pi.removesuffix('genial')
print(Coisa_ruim)

# 2.12
import this