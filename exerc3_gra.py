import random

# Lista de palavras 
palavras = ["abela", "balas", "cachos", "dedos", "esfera", "fazia", "gatos", "haste", "irado", "jovem", "kafka", "lares", "mimos", "neve", "olhar", "papel", "quase", "rosas", "salto", "tampa", "umbra", "vazio", "xerox", "zombar"]

# Escolhe uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# Número de tentativas disponíveis
tentativas = 6
letras_corretas = []        # Lista para armazenar letras corretamente adivinhadas
letras_incorretas = []      # Lista para armazenar letras incorretamente adivinhadas

print("Bem-vindo !")
print("Adivinhe a palavra de 5 letras.")

# Função para mostrar a palavra oculta com letras adivinhadas
def mostrar_palavra_oculta(palavra_secreta, letras_corretas):
    resultado = ""
    for letra in palavra_secreta:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Loop principal 
while tentativas > 0:
    palavra_oculta = mostrar_palavra_oculta(palavra_secreta, letras_corretas)
    print(f"Palavra atual: {palavra_oculta}")

    if letras_incorretas:
        print(f"Tentativas incorretas: {', '.join(letras_incorretas)}")

    tentativa = input("Digite uma palavra de 5 letras: ").lower()

    if len(tentativa) == 5:
        if tentativa == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra!")
            break
        else:
            letras_corretas_temp = []
            letras_incorretas_temp = []
            for i, letra in enumerate(tentativa):
                if letra == palavra_secreta[i]:
                    letras_corretas_temp.append(letra)
                elif letra in palavra_secreta:
                    letras_incorretas_temp.append(letra)

            letras_corretas += letras_corretas_temp
            letras_incorretas += letras_incorretas_temp
            tentativas -= 1

            print(f"Letras corretas no lugar errado: {', '.join(letras_corretas_temp)}")
            print(f"Letras corretas no lugar certo: {', '.join(letras_corretas)}")
            print(f"Tentativas incorretas: {', '.join(letras_incorretas_temp)}")

    else:
        print("Por favor, digite uma palavra de 5 letras válida.")

if tentativas == 0:
    print(f"Fim de jogo! A palavra correta era: {palavra_secreta}")
