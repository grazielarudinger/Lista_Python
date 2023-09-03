# Função para criar um tabuleiro vazio com tamanho NxN
def criar_tabuleiro(n):
    return [[" " for _ in range(n)] for _ in range(n)]

# Função para mostrar o tabuleiro na saída padrão
def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))  
        print("-" * (4 * len(linha) - 1))  

# Função para verificar se há um vencedor na posição atual (linha, coluna)
def verificar_ganhador(tabuleiro, jogador, linha, coluna):
    n = len(tabuleiro)

   

# Função principal do jogo
def jogar_jogo():
    print("Bem-vindo ao Jogo da Velha NxN!")
    n = int(input("Digite o tamanho do tabuleiro (NxN): "))
    
    tabuleiro = criar_tabuleiro(n)
    jogador_atual = "X"
    
    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")
        
        linha = int(input(f"Digite a linha (0 a {n-1}) para {jogador_atual}: "))
        coluna = int(input(f"Digite a coluna (0 a {n-1}) para {jogador_atual}: "))
        
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_ganhador(tabuleiro, jogador_atual, linha, coluna):
                mostrar_tabuleiro(tabuleiro)
                print(f"O jogador {jogador_atual} venceu!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

if __name__ == "__main__":
    jogar_jogo()
