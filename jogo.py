import random

# Escolhendo a dificuldade
print("Bem-vindo ao Jogo da Adivinhação!")
nivel = input("Escolha a dificuldade (fácil/difícil): ").lower()

if nivel == "fácil":
    sorteio = random.randint(1, 20)
    max_tentativas = 5
    vidas = None  # No modo fácil, não usamos vidas
elif nivel == "difícil":
    sorteio = random.randint(1, 50)
    max_tentativas = 5
    vidas = 3  # No modo difícil, o jogador tem 3 vidas
else:
    print("Opção inválida! Começaremos no modo fácil.")
    sorteio = random.randint(1, 20)
    max_tentativas = 5
    vidas = None

tentativas = 0

name = input("Digite seu nome: ")

# Jogo fácil
if nivel == "fácil":
    while tentativas < max_tentativas:
        usuario_str = input(f"{name}, digite um número entre 1 e 20: ")

        # Conferindo se o input é um número válido
        if not usuario_str.isdigit():
            print(f"Por favor {name}, digite apenas números.")
            continue

        usuario = int(usuario_str)

        if usuario == sorteio:
            print(f"Acertou, Parabéns {name}! Você acertou em {tentativas + 1} tentativa(s)!")
            break
        elif usuario > sorteio:
            print("O seu número foi maior!")
        else:
            print("O seu número foi menor que o sorteado.")

        tentativas += 1

# Jogo difícil
elif nivel == "difícil":
    while tentativas < max_tentativas and vidas > 0:
        usuario_str = input(f"{name}, digite um número entre 1 e 50: ")

        # Conferindo se o input é um número válido
        if not usuario_str.isdigit():
            print(f"Por favor {name}, digite apenas números.")
            continue

        usuario = int(usuario_str)

        if usuario == sorteio:
            print(f"Acertou, Parabéns {name}! Você acertou em {tentativas + 1} tentativa(s) com {vidas} vida(s) restantes!")
            break
        elif usuario > sorteio:
            vidas -= 1
            print(f"Seu número foi maior! Cuidado, agora você tem {vidas} vida(s).")
        else:
            vidas -= 1
            print(f"Seu número foi menor que o sorteado! Atenção, agora você tem {vidas} vida(s).")

        tentativas += 1

# Fim do jogo
if tentativas == max_tentativas or (vidas is not None and vidas == 0):
    if nivel == "difícil":
        print(f"Fim de jogo {name}! O número sorteado era {sorteio}. Suas vidas acabaram... Vamos tentar novamente?")
    else:
        print(f"Fim de jogo {name}! O número sorteado era {sorteio}. Vamos tentar novamente?")