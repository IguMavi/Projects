import random
from palavras import lista_palavras

palavra = random.choice(lista_palavras)

contador = len(palavra)
check = False
sla = ['_' for _ in range(len(palavra))]
quantidade = len(palavra)

while(check == False):
    tentativa = input()
    quantidade -= 1
    if(quantidade == 0):
        print("Acabou as tentativas")
        print(f"A palavra era: {palavra}")
        break
    if(len(tentativa) == 1):
        for i in range(len(palavra)):
            if(tentativa == palavra[i]):
                contador -= 1
                sla[i] = tentativa
        print(*sla)
    else:
        if(tentativa == palavra):
            print(f"Acertou em {len(palavra)-quantidade} tentativas!!")
            break
    print(f"Faltam {quantidade} tentativas")
    
