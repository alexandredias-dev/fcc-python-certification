# 1. Pegando os dados do usuário (os inputs)
# Usamos int() porque o input sempre recebe o texto, e precisamos de números
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo (pular de quanto em quanto): "))

# 2. Criando a lógica da sequência
print(f"\nContando de {inicio} até {fim}, pulando de {passo} em {passo}:")

# O range precisa de (inicio, fim + 1, passo) 
# Usamos 'fim + 1' porque o Python sempre para um número ANTES do final
for contagem in range(inicio, fim + 1, passo):
    print(contagem, end=" -> ")

print("FIM!")