# Função para validar a transitividade
def checar_transitividade(R):
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                return False
    return True

# Input dos elementos de A (não é necessário, mas achei melhor incluir para a representação)
A = set(map(int, input("Digite os elementos do conjunto A (separados por espaço): ").split()))
# Declaração da endorelação R
R = set()
# Input da quantia de pares de R
n = int(input("Quantos pares compõem a relação R? "))
# Laço para incluir os pares em R
for _ in range(n):
    a, b = map(int, input("Digite um par (a b): ").split())
    R.add((a, b))

print("A relação é transitiva?", checar_transitividade(R))
