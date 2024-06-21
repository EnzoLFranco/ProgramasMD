# Função para adicionar os pares necessários para cumprir com a necessidade
def fecho_transitivo(A, R):
    fecho = R.copy()
    add = True
    while add:
        add = False
        novos_pares = set()
        for (a, b) in fecho:
            for (c, d) in fecho:
                if b == c and (a, d) not in fecho:
                    novos_pares.add((a, d))
        if novos_pares:
            fecho.update(novos_pares)
            add = True
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

print("Fecho transitivo de R:", fecho_transitivo(A, R))