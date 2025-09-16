estoque_atual = {
    "canetas": 150,
    "cadernos": 95,
    "borrachas": 40,
    "lapis": 200,
    "marcadores": 70,
    "folhas A4": 120,
    "réguas": 60,
    "pastas": 30
}

movimentacoes_dia = [
    ("canetas", "saída", 25),
    ("cadernos", "entrada", 10),
    ("borrachas", "saída", 15),
    ("lapis", "saída", 50),
    ("marcadores", "entrada", 20),
    ("pastas", "entrada", 15),
    ("réguas", "saída", 25),
    ("canetas", "entrada", 40),
    ("folhas A4", "saída", 30),
    ("lapis", "entrada", 60),
    ("borrachas", "entrada", 20),
    ("marcadores", "saída", 10),
    ("cadernos", "saída", 40),
    ("clips", "entrada", 100),
    ("pastas", "saída", 20)
]

for produto, tipo, quantidade in movimentacoes_dia:
    if produto not in estoque_atual:
        estoque_atual[produto] = 0
    if tipo == "entrada":
        estoque_atual[produto] += quantidade
    elif tipo == "saída":
        estoque_atual[produto] -= quantidade

produtos_reposicao = [p for p, q in estoque_atual.items() if q <= 50]

print("\n=== RELATÓRIO FINAL DO ESTOQUE ===")
for produto, quantidade in estoque_atual.items():
    print(f"{produto}: {quantidade} unidades")

print("\n=== PRODUTOS QUE PRECISAM DE REPOSIÇÃO ===")
if produtos_reposicao:
    for produto in produtos_reposicao:
        print(f"- {produto} (estoque: {estoque_atual[produto]})")
else:
    print("Nenhum produto precisa de reposição no momento.")
