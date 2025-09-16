# Sistema de Controle de Estoque - Armazém Central

# Estoque inicial (mínimo de 8 itens)
estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "borrachas": 60,
    "lápis": 200,
    "marcadores": 75,
    "papel A4": 500,
    "grampeadores": 40,
    "post-its": 120,
}

# Movimentações do dia (mínimo de 15 operações)
movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 30),
    ("lápis", "saída", 60),
    ("marcadores", "entrada", 15),
    ("papel A4", "saída", 200),
    ("grampeadores", "entrada", 20),
    ("post-its", "saída", 50),
    ("cola", "entrada", 80),          # novo item
    ("tesouras", "entrada", 40),      # novo item
    ("canetas", "saída", 50),
    ("cadernos", "saída", 30),
    ("borrachas", "entrada", 20),
    ("papel A4", "saída", 100),
    ("tesouras", "saída", 10),
]

# Processamento das movimentações
for produto, tipo, quantidade in movimentacoes_dia:
    if produto not in estoque_atual:
        estoque_atual[produto] = 0  # adiciona produto novo

    if tipo == "entrada":
        estoque_atual[produto] += quantidade
    elif tipo == "saída":
        estoque_atual[produto] -= quantidade
    else:
        print(f"Tipo de movimentação inválido para {produto}: {tipo}")

# Identificação de produtos com estoque baixo
reposicao = [p for p, q in estoque_atual.items() if q <= 50]

# Relatório final
print("\n=== RELATÓRIO FINAL DO ESTOQUE ===")
for produto, quantidade in estoque_atual.items():
    print(f"{produto.capitalize():<15} -> {quantidade} unidades")

print("\n=== PRODUTOS QUE PRECISAM DE REPOSIÇÃO ===")
if reposicao:
    for produto in reposicao:
        print(f"- {produto.capitalize()} (estoque: {estoque_atual[produto]})")
else:
    print("Nenhum produto precisa de reposição!")
