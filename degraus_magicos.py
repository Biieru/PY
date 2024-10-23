import random #pra deixar o n randomizado e nn ser o msm sempre
 
def escadaria_magica():
    # Definindo o degrau alvo n como um número aleatório entre 1 e 100 pra facilitar ne KSKSKS
    n = random.randint(1, 100)
    degrau_atual = 0
    movimentos = 0
 
    print("Bem-vindo à escadaria mágica! Alcance o degrau mágico que está entre o número 1 e 100, você tem 10 movimentos para alcançar o correto!")
 
    # Loop para realizar até 10 moves (game over) ou até atingir o degrau n (win)
    while movimentos < 10:
        print(f"Você está no degrau {degrau_atual}.")
        
        # Entrada do valor de k
        k = int(input("Quantos degraus você vai subir? (Numero positivo para subir, numero negativo para descer): "))
        
        # Se o degrau atual for par, sobe k degraus
        if degrau_atual % 2 == 0:
            degrau_atual += k
        else:  # Se o degrau atual for ímpar, desce k degraus
            degrau_atual -= k
        
        # Se o degrau atual for menor que 0, volta para 0, não existe subsolo kdks
        if degrau_atual < 0:
            degrau_atual = 0
        
        movimentos += 1
 
        # Verifica se atingiu o degrau n para win
        if degrau_atual == n:
            print(f"Parabéns! Você chegou ao degrau {n} em {movimentos} movimentos.")
            return
        
        # Dica de mais alto ou mais baixo de acordo com o que o usuario inputou
        if degrau_atual < n:
            print("Poxa, o andar que você procura está mais alto!")
        elif degrau_atual > n:
            print("Poxa, o andar que você procura está mais baixo!")
 
    # Se não atingiu o degrau n após 10 movimentos
    print(f"Você não conseguiu alcançar o degrau {n} em 10 movimentos... GAME OVER")
 
# Executando o jogo
escadaria_magica()