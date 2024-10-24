print = ("BEM VINDO A BALADA DO DUDU!")
idade = int(input("\nDigite a sua idade: "))

if idade >= 18:
    print("Você pode entrar!")

elif idade >=16:
    autorizacao = input("Você tem uma autorização?")
    if autorizacao == "SIM":
        print("Você pode entrar!")
    else:
        print("Você não pode entrar!")
else:
    print("Você é menor de idade, não pode entrar!")

