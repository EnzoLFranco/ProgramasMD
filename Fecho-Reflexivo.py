# Função para adicionar os pares necessários para cumprir com a necessidade
def fecho_reflexivo(A, R):
    fecho = R.copy()
    for a in A:
        fecho.add((a, a))
    return fecho

# Input dos elementos de A
A = set(map(int, input("Digite os elementos do conjunto A (separados por espaço): ").split()))
# Declaração da endorelação R
R = set()
# Input da quantia de pares de R
n = int(input("Quantos pares compõem a relação R? "))
# Laço para incluir os pares em R
for _ in range(n):
    a, b = map(int, input("Digite um par (a b): ").split())
    R.add((a, b))

print("Fecho reflexivo de R:", fecho_reflexivo(A, R))