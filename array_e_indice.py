def imprime_nomes():
    nomes = ["João", "Maria", "Fulano", "Ciclano"]
    print("1 - " + nomes[0])
    print("2 - " + nomes[1])
    print("3 - " + nomes[2])
    print("4 - " + nomes[3])

imprime_nomes()

def imprime_nomes2():
    nomes = ["João", "Maria", "Fulano", "Beltrano"]
    print("1 - " + nomes[0])
    print("4 - " + nomes[3])

imprime_nomes2()

def imprime_nomes3():
    nomes = ["João", "Maria", "Fulano", "Beltrano"]
    print("2 - " + nomes[1])
    print("3 - " + nomes[2])

imprime_nomes3()

def imprime_listadealimentos():
    array_inicial = ["Macarrão", "Pepino", "Batata"]
    array_inicial[0] = str(input("Digite um alimento: "))
    array_inicial[1] = str(input("Digite outro alimento: "))
    array_inicial[2] = str(input("Digite outro alimento: "))
    print("1 - " + array_inicial[0])
    print("2 - " + array_inicial[1])
    print("3 - " + array_inicial[2])

imprime_listadealimentos()