def imprime_nomes():
    nomes = ["João", "Maria", "Fulano", "Ciclano"]
    print("1 - " + nomes[0])
    print("2 - " + nomes[1])
    print("3 - " + nomes[2])
    print("4 - " + nomes[3] + "\n")

imprime_nomes()

def imprime_nomes2():
    nomes = ["João", "Maria", "Fulano", "Beltrano"]
    print("1 - " + nomes[0])
    print("4 - " + nomes[3] + "\n")

imprime_nomes2()

def imprime_nomes3():
    nomes = ["João", "Maria", "Fulano", "Beltrano"]
    print("2 - " + nomes[1])
    print("3 - " + nomes[2] + "\n")

imprime_nomes3()

valor1 = str(input("Digite um alimento: "))
valor2 = str(input("Digite outro alimento: "))
valor3 = str(input("Digite outro alimento: "))

def imprime_listadealimentos(valor1, valor2, valor3):
    array_inicial = ["Macarrão", "Pepino", "Batata"]
    array_inicial[0] = valor1
    array_inicial[1] = valor2
    array_inicial[2] = valor3
    print("1 - " + array_inicial[0])
    print("2 - " + array_inicial[1])
    print("3 - " + array_inicial[2])

imprime_listadealimentos()