# Função para validar a reflexividade
def checar_reflexividade(A, R):
    for a in A:
        if (a, a) not in R:
            return False
    return True

# Input dos elementos de A (não é necessário, mas achei melhor incluir para a representação)
A = set(map(int, input("Digite os elementos do conjunto A (separados por espaço): ").split()))
# Declaração da endorelação R
R = set()
# Input da quantia de pares de R
n = int(input("Quantos pares compõem a endorelação R? "))
# Laço para incluir os pares em R
for _ in range(n):
    a, b = map(int, input("Digite um par (a b): ").split())
    R.add((a, b))

print("A relação é reflexiva?", checar_reflexividade(A, R))