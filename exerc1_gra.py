
# função cria um tabuleiro 4x4
def criar_tabuleiro_4x4():
    return [[" " for _ in range(4)] for _ in range(4)]

# Para que os jogadores possam ver o tabuleiro,
# é criada uma função que o exibe na tela. 
def exibir_tabuleiro_4x4(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (7 * len(linha) - 1))
# função para verificar quem ganhou,
# Preencher todas as células em uma linha horizontal.
# Preencher todas as células em uma coluna vertical.
# Preencher todas as células na diagonal principal.
# Preencher todas as células na diagonal secundária.
def verificar_ganhou_4x4(tabuleiro, jogador, linha, coluna):
  
    if all(tabuleiro[linha][i] == jogador for i in range(4)) or all(tabuleiro[i][coluna] == jogador for i in range(4)):
        return True

    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False
# função principal
def jogar_jogo_da_velha_4x4():
    print("Olá, vamos jogar um jogo da velha?")
    
    tabuleiro = criar_tabuleiro_4x4()
    jogador_atual = "X"
    
    for _ in range(16):
        exibir_tabuleiro_4x4(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")
        
        while True:
            linha = int(input("Digite a linha (0 a 3): "))
            coluna = int(input("Digite a coluna (0 a 3): "))
            
            if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == " ":
                break
            else:
                print("Sua posição está inválida. Tente novamente.")
        
        tabuleiro[linha][coluna] = jogador_atual
        
        if verificar_ganhou_4x4(tabuleiro, jogador_atual, linha, coluna):
            exibir_tabuleiro_4x4(tabuleiro)
            print(f"O jogador {jogador_atual} venceu!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"
    
    else:
        exibir_tabuleiro_4x4(tabuleiro)
        print("O jogo terminou em empate!")

if __name__ == "__main__":
    jogar_jogo_da_velha_4x4()
